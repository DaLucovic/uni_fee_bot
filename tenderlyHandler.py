import requests
import json
from web3 import Web3
from eth_abi import decode
from constants import RPC_BASE_URL, API_BASE_URL
from pathlib import Path
import time

class TenderlyHandler:
    def __init__(self, network_id="1"):
        try:
            from authent import creds_dict

            creds = creds_dict['tenderly']

            required_keys = ['account_name', 'project_name', 'access_token', 'rpc_key']
            if not all(key in creds for key in required_keys):
                raise ValueError('Required Tenderly credentials are missing in authent.py')
        except Exception as e:
            raise ValueError('Not able to instantiate TenderlySimulator with required credentials, please check error: ' + e)


        self.base_url = (API_BASE_URL.format(account_name=creds['account_name'], project_name=creds['project_name']))
        self.headers = {
            "X-Access-Key": creds['access_token'],
            "Content-Type": "application/json",
        }
        self.network_id = network_id
        self.rpc_url = RPC_BASE_URL + creds_dict['tenderly']['rpc_key']
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
        self.abi_cache_dir = Path("abi_cache")
        self.abi_cache_dir.mkdir(exist_ok=True)

    def _encode_function_call(self, contract_address, abi, function_name, args):
        contract_address = self.w3.to_checksum_address(contract_address)
        contract = self.w3.eth.contract(address=contract_address, abi=abi)

        try:
            fn = contract.get_function_by_name(function_name)(*(args or []))
        except ValueError as e:
            raise ValueError(
                f"Function '{function_name}' not found or invalid arguments"
            ) from e

        return fn._encode_transaction_data(), fn.abi

    def simulate_transaction(
        self,
        from_address,
        to_address,
        data="0x",
        value_wei=0,
        gas=8_000_000,
    ):
        payload = {
            "network_id": self.network_id,
            "from": self.w3.to_checksum_address(from_address),
            "to": self.w3.to_checksum_address(to_address),
            "input": data,
            "value": hex(value_wei),
            "gas": gas,
        }

        response = requests.post(
            self.base_url,
            headers=self.headers,
            data=json.dumps(payload),
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"Tenderly simulation failed: {response.status_code} {response.text}"
            )

        return response.json()

    def simulate_read(self, contract_address: str, method_name: str):
        payload = {
            "jsonrpc": "2.0",
            "method": "tenderly_getContractAbi",
            "params": [contract_address],
            "id": self.network_id
        }

        response = self.w3.provider.make_request(payload['method'], payload['params'])

        abi = response.get("result")
        if not abi:
            raise Exception(f"ABI not found for contract {contract_address}")

        contract = self.w3.eth.contract(address=contract_address, abi=abi)
        contract_function = getattr(contract.functions, method_name)

        return contract_function.call()

    def simulate_write(
        self,
        from_address,
        contract_address,
        abi,
        function_name,
        args=None,
        value_wei=0,
    ):
        calldata, fn_abi = self._encode_function_call(
            contract_address, abi, function_name, args
        )

        if fn_abi["stateMutability"] in ("view", "pure"):
            raise ValueError("Attempted to write-call a view/pure function")

        return self.simulate_transaction(
            from_address=from_address,
            to_address=contract_address,
            data=calldata,
            value_wei=value_wei,
        )

    def get_contract_abi(self, contract_address: str):
        address = contract_address.lower()
        abi_path = self.abi_cache_dir / '0x1d42064fc4beb5f8aaf85f4617ae8b3b5b8bd801.json' #self.abi_cache_dir / f"{address}.json"

        if abi_path.exists():
            with open(abi_path) as f:
                print('ABI found locally!')
                return json.load(f)

        payload = {
            "jsonrpc": "2.0",
            "method": "tenderly_getContractAbi",
            "params": [contract_address],
            "id": self.network_id
        }

        response = self.w3.provider.make_request(
            payload["method"],
            payload["params"]
        )

        abi = response.get("result")
        if not abi:
            raise Exception(f"ABI not found for contract {contract_address}")
        else:
            print('ABI found, sleeping for 60 sec to respect API rate limit')
            time.sleep(60)

        with open(abi_path, "w") as f:
            json.dump(abi, f, indent=2)

        return abi

    def batch_call_methods(self, contract_address: str, method_names: list, from_address: str = None):
        """
        Batch-call multiple read-only methods on a contract using Tenderly's RPC.

        Args:
            contract_address (str): The contract address to call.
            method_names (list): List of method names (no arguments supported yet).
            from_address (str, optional): Optional 'from' address for the call. Defaults to None.

        Returns:
            dict: Mapping of method name -> decoded result
        """
        contract_address = self.w3.to_checksum_address(contract_address)
        abi = self.get_contract_abi(contract_address)
        contract = self.w3.eth.contract(address=contract_address, abi=abi)

        batch_payload = []
        for i, method_name in enumerate(method_names):
            func = getattr(contract.functions, method_name)
            data = func()._encode_transaction_data()
            params = {"to": contract_address, "data": data}
            if from_address:
                params["from"] = from_address

            batch_payload.append({
                "jsonrpc": "2.0",
                "id": i,
                "method": "eth_call",
                "params": [params, "latest"]
            })

        try:
            response = requests.post(self.rpc_url, json=batch_payload)
            response.raise_for_status()
            response_json = response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Tenderly batch call failed: {e}")
        except json.JSONDecodeError:
            raise RuntimeError("Tenderly response was not valid JSON")

        results = {}
        for res in response_json:
            idx = res["id"]
            method_name = method_names[idx]

            if "error" in res:
                results[method_name] = {"error": res["error"]}
                continue

            hex_result = res.get("result", "0x")
            func = getattr(contract.functions, method_name)
            try:
                types = [o["type"] for o in func.abi["outputs"]]
                decoded = decode(types, bytes.fromhex(hex_result[2:]))
                # Unwrap single-value outputs
                if len(decoded) == 1:
                    decoded = decoded[0]
            except Exception as e:
                decoded = {"error": f"Decoding failed: {e}"}

            results[method_name] = decoded

        return results

if __name__ == "__main__":
    simulator = TenderlyHandler()

    result = simulator.simulate_read(
        contract_address="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        method_name="name"
    )

    result = simulator.batch_call_methods(
        contract_address="0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        method_names=["name", 'totalSupply']
    )

    # result = simulator.simulate_contract_call(
    #     from_address="0x0000000000000000000000000000000000000000",
    #     contract_address="0x5E74C9f42EEd283bFf3744fBD1889d398d40867d",
    #     function_name="collect",
    # args=[{"pool":"0x4e68ccd3e89f51c3074ca5072bbac773960dfa36","amount0Requested":"340282366920938463463374607431768211455","amount1Requested":"340282366920938463463374607431768211455"},{"pool":"0xe8f7c89c5efa061e340f2d2f206ec78fd8f7e124","amount0Requested":"340282366920938463463374607431768211455","amount1Requested":"340282366920938463463374607431768211455"}])

    print(result)
