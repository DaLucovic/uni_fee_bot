import json, requests
from constants import DL_PRICE_LIST_URL
from tenderlyHandler import TenderlyHandler
import pandas as pd

def load_uniswap_metadata():
    with open("v3_tokens.json") as f:
        tokens = json.load(f)

    with open("v3_pools.json") as f:
        pools = json.load(f)

    return tokens, pools

def get_current_prices(tokens):
    token_addresses = tokens.keys()
    price_ids = [f"ethereum:{addr}" for addr in token_addresses]

    price_url = DL_PRICE_LIST_URL.format(list=",".join(price_ids))
    raw_data = requests.get(price_url)
    data = json.loads(raw_data.content)

    return data

if __name__ == "__main__":
    tokens, pools = load_uniswap_metadata()
    prices = get_current_prices(tokens)['coins']

    handler = TenderlyHandler()

    return_dict = {}

    for pool in pools:
        pool_metadata = pools[pool]

        func = 'protocolFees'
        result = handler.batch_call_methods(pool, [func])

        token0 = pools[pool]['token0']
        token1 = pools[pool]['token1']

        token0_amount = result[func][0] / (10**tokens[token0]['decimals'])
        token1_amount = result[func][1] / (10**tokens[token1]['decimals'])

        token0_value = token0_amount * prices[f'ethereum:{token0}']['price']
        token1_value = token1_amount * prices[f'ethereum:{token1}']['price']

        data = {
            'name': pool_metadata['name'],
            'token0': token0,
            'token1': token1,
            'token0_amount': token0_amount,
            'token1_amount': token1_amount,
            'token0_value': token0_value,
            'token1_value': token1_value,
            'total_accrued_value': token0_value + token1_value,
        }

        return_dict[pool] = data

    return_df = pd.DataFrame(return_dict).T
    print(return_dict)