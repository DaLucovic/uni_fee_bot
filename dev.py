import requests
import json
from web3 import Web3
from abis import V3FeeAdapter  # Import your ABI here

class TenderlySimulator:
    def __init__(self, account_name, project_name, access_token, network_id="1"):
        self.base_url = f"https://api.tenderly.co/api/v1/account/{account_name}/project/{project_name}/simulate"
        self.headers = {
            "X-Access-Key": access_token,
            "Content-Type": "application/json"
        }
        self.network_id = network_id
        self.w3 = Web3()

    def simulate_transaction(self, from_address, to_address, value_wei=0, data="0x"):
        payload = {
            "network_id": self.network_id,
            "from": from_address,
            "to": to_address,
            "input": data,
            "value": hex(value_wei)
        }

        response = requests.post(self.base_url, headers=self.headers, data=json.dumps(payload))
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Simulation failed: {response.status_code} {response.text}")

    def simulate_contract_call(self, from_address, contract_address, function_name, args=None, value_wei=0):
        """
        Simulate a smart contract function call using the imported ABI.
        """
        contract = self.w3.eth.contract(address=contract_address, abi=V3FeeAdapter)

        # Check if the function exists in the ABI
        try:
            function = contract.get_function_by_name(function_name)(*(args or []))
        except ValueError:
            raise ValueError(f"Function '{function_name}' not found in ABI.")

        print(function.abi)  # shows inputs, outputs, types
        print(args)  # check the values you're passing

        calldata = function._encode_transaction_data()

        return self.simulate_transaction(
            from_address=from_address,
            to_address=contract_address,
            value_wei=value_wei,
            data=calldata
        )


# Example usage
if __name__ == "__main__":
    simulator = TenderlySimulator(
        account_name="LucFortera",
        project_name="Project",
        access_token="orSYdfy8N43QE-mvts0Fn9pCW8O8dP-G"
    )

    result = simulator.simulate_contract_call(
        from_address="0x0000000000000000000000000000000000000000",
        contract_address="0x5e74c9f42eed283bff3744fbd1889d398d40867d",
        function_name="collect",
        args=[{"pool":"0x4e68ccd3e89f51c3074ca5072bbac773960dfa36","amount0Requested":"340282366920938463463374607431768211455","amount1Requested":"340282366920938463463374607431768211455"},{"pool":"0xe8f7c89c5efa061e340f2d2f206ec78fd8f7e124","amount0Requested":"340282366920938463463374607431768211455","amount1Requested":"340282366920938463463374607431768211455"}]
    )

    print(json.dumps(result, indent=2))
