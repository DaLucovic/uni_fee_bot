from tenderlyHandler import TenderlyHandler
from app import load_uniswap_metadata

handler = TenderlyHandler()

tokens, pools = load_uniswap_metadata()

for pool in pools:
    handler.get_contract_abi(pool)