import json
import requests

# 1) Provide your Graph API key
API_KEY = "c017cb5fe0b262c431ba9bfce11b5719"

# 2) Subgraph endpoint
SUBGRAPH_URL = f"https://gateway.thegraph.com/api/{API_KEY}/subgraphs/id/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV"

# 3) GraphQL query: top 50 pools by TVL
query = """
{
  pools(first: 100, orderBy: volumeUSD, orderDirection: desc) {
    id
    feeTier
    token0 {
      id
      symbol
      decimals
    }
    token1 {
      id
      symbol
      decimals
    }
  }
}
"""

response = requests.post(SUBGRAPH_URL, json={"query": query})
data = response.json()

Tokens = {}
V3Pools = {}

for pool in data["data"]["pools"]:
    pool_addr = pool["id"]
    fee_tier = int(pool["feeTier"]) / 10000  # convert to % (e.g. 3000 -> 0.3)

    t0 = pool["token0"]
    t1 = pool["token1"]

    # token metadata
    Tokens[t0["id"]] = {
        "symbol": t0["symbol"],
        "decimals": int(t0["decimals"])
    }
    Tokens[t1["id"]] = {
        "symbol": t1["symbol"],
        "decimals": int(t1["decimals"])
    }

    pool_name = f"{t0['symbol']}/{t1['symbol']} ({fee_tier}%)"

    # pool entry
    V3Pools[pool_addr] = {
        "name": pool_name,
        "token0": t0["id"],
        "token1": t1["id"],
        "fee_tier": fee_tier
    }

# 4) Write JSON files for future use
with open("v3_tokens.json", "w") as f:
    json.dump(Tokens, f, indent=4)

with open("v3_pools.json", "w") as f:
    json.dump(V3Pools, f, indent=4)

print("Done! Saved v3_tokens.json and v3_pools.json")
