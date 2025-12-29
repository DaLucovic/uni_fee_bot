import json

V3FeeAdapter = json.loads("""[
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "_factory",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "_tokenJar",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "function",
      "name": "setMerkleRoot",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "_merkleRoot",
          "type": "bytes32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "TOKEN_JAR",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "collect",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "collectParams",
          "type": "tuple[]",
          "storage_location": "default",
          "components": [
            {
              "name": "pool",
              "type": "address",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "address"
              }
            },
            {
              "name": "amount0Requested",
              "type": "uint128",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "uint"
              }
            },
            {
              "name": "amount1Requested",
              "type": "uint128",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "uint"
              }
            }
          ],
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice"
          }
        }
      ],
      "outputs": [
        {
          "name": "amountsCollected",
          "type": "tuple[]",
          "storage_location": "default",
          "components": [
            {
              "name": "amount0Collected",
              "type": "uint128",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "uint"
              }
            },
            {
              "name": "amount1Collected",
              "type": "uint128",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "uint"
              }
            }
          ],
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "enableFeeAmount",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "fee",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tickSpacing",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "feeTiers",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "setFactoryOwner",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "newOwner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "storeFeeTier",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "feeTier",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "transferOwnership",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "newOwner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "setDefaultFeeByFeeTier",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "feeTier",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "defaultFeeValue",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "setFeeSetter",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "newFeeSetter",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "triggerFeeUpdate",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "token0",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "token1",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "proof",
          "type": "bytes32[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "bytes"
            }
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "FACTORY",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "defaultFees",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "feeTier",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "defaultFeeValue",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "merkleRoot",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "bytes32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "batchTriggerFeeUpdate",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "pairs",
          "type": "tuple[]",
          "storage_location": "default",
          "components": [
            {
              "name": "token0",
              "type": "address",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "address"
              }
            },
            {
              "name": "token1",
              "type": "address",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "address"
              }
            }
          ],
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice"
          }
        },
        {
          "name": "proof",
          "type": "bytes32[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "bytes"
            }
          }
        },
        {
          "name": "proofFlags",
          "type": "bool[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "bool"
            }
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "feeSetter",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "owner",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "triggerFeeUpdate",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "pool",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "proof",
          "type": "bytes32[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "bytes"
            }
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "event",
      "name": "OwnershipTransferred",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "user",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "newOwner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": null
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    },
    {
      "type": "event",
      "name": "Burn",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "owner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "Collect",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "owner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "Flash",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "sender",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "paid0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "paid1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "Initialize",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "sqrtPriceX96",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tick",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "Mint",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "sender",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "owner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "CollectProtocol",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "sender",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "amount0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "IncreaseObservationCardinalityNext",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "observationCardinalityNextOld",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "observationCardinalityNextNew",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "SetFeeProtocol",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "feeProtocol0Old",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeProtocol1Old",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeProtocol0New",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeProtocol1New",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "Swap",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "sender",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "amount0",
          "type": "int256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount1",
          "type": "int256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "sqrtPriceX96",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "liquidity",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tick",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": null
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    },
    {
      "type": "function",
      "name": "collectProtocol",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "amount0Requested",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1Requested",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "amount0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "setFeeProtocol",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "feeProtocol0",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeProtocol1",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": []
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    },
    {
      "type": "function",
      "name": "FACTORY",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "feeTiers",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "i",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "merkleRoot",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "bytes32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "setDefaultFeeByFeeTier",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "feeTier",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "defaultFeeValue",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "batchTriggerFeeUpdate",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "pairs",
          "type": "tuple[]",
          "storage_location": "default",
          "components": [
            {
              "name": "token0",
              "type": "address",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "address"
              }
            },
            {
              "name": "token1",
              "type": "address",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "address"
              }
            }
          ],
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice"
          }
        },
        {
          "name": "proof",
          "type": "bytes32[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "bytes"
            }
          }
        },
        {
          "name": "proofFlags",
          "type": "bool[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "bool"
            }
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "collect",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "collectParams",
          "type": "tuple[]",
          "storage_location": "default",
          "components": [
            {
              "name": "pool",
              "type": "address",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "address"
              }
            },
            {
              "name": "amount0Requested",
              "type": "uint128",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "uint"
              }
            },
            {
              "name": "amount1Requested",
              "type": "uint128",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "uint"
              }
            }
          ],
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice"
          }
        }
      ],
      "outputs": [
        {
          "name": "amountsCollected",
          "type": "tuple[]",
          "storage_location": "default",
          "components": [
            {
              "name": "amount0Collected",
              "type": "uint128",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "uint"
              }
            },
            {
              "name": "amount1Collected",
              "type": "uint128",
              "storage_location": "default",
              "offset": 0,
              "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "indexed": false,
              "simple_type": {
                "type": "uint"
              }
            }
          ],
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "feeSetter",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "storeFeeTier",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "feeTier",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "TOKEN_JAR",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "setFeeSetter",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "newFeeSetter",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "setMerkleRoot",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "_merkleRoot",
          "type": "bytes32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "triggerFeeUpdate",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "pool",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "merkleProof",
          "type": "bytes32[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "bytes"
            }
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "triggerFeeUpdate",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "token0",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "token1",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "proof",
          "type": "bytes32[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "bytes"
            }
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "defaultFees",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "feeTier",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "defaultFeeValue",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "enableFeeAmount",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "newFeeTier",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tickSpacing",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "setFactoryOwner",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "newOwner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": []
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    },
    {
      "type": "function",
      "name": "feeAmountTickSpacing",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "fee",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "getPool",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "tokenA",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tokenB",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "fee",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "pool",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "owner",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "setOwner",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "_owner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "createPool",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "tokenA",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tokenB",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "fee",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "pool",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "enableFeeAmount",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "fee",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tickSpacing",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "event",
      "name": "OwnerChanged",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "oldOwner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "newOwner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "PoolCreated",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "token0",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "token1",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "fee",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tickSpacing",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "pool",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "FeeAmountEnabled",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "fee",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tickSpacing",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": null
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    },
    {
      "type": "function",
      "name": "increaseObservationCardinalityNext",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "observationCardinalityNext",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "initialize",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "sqrtPriceX96",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "mint",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "data",
          "type": "bytes",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ],
      "outputs": [
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "swap",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "zeroForOne",
          "type": "bool",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bool"
          }
        },
        {
          "name": "amountSpecified",
          "type": "int256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "sqrtPriceLimitX96",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "data",
          "type": "bytes",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ],
      "outputs": [
        {
          "name": "amount0",
          "type": "int256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount1",
          "type": "int256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "burn",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "collect",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount0Requested",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1Requested",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "amount0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "flash",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "data",
          "type": "bytes",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ],
      "outputs": []
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    },
    {
      "type": "function",
      "name": "observe",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "secondsAgos",
          "type": "uint32[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "uint"
            }
          }
        }
      ],
      "outputs": [
        {
          "name": "tickCumulatives",
          "type": "int56[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "int"
            }
          }
        },
        {
          "name": "secondsPerLiquidityCumulativeX128s",
          "type": "uint160[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "uint"
            }
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "snapshotCumulativesInside",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": [
        {
          "name": "tickCumulativeInside",
          "type": "int56",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "secondsPerLiquidityInsideX128",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "secondsInside",
          "type": "uint32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    },
    {
      "type": "function",
      "name": "owner",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "transferOwnership",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "newOwner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "event",
      "name": "OwnershipTransferred",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "user",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "newOwner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        }
      ],
      "outputs": null
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    },
    {
      "type": "function",
      "name": "feeGrowthGlobal0X128",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "liquidity",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "observations",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "index",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "blockTimestamp",
          "type": "uint32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tickCumulative",
          "type": "int56",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "secondsPerLiquidityCumulativeX128",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "initialized",
          "type": "bool",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bool"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "positions",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "key",
          "type": "bytes32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ],
      "outputs": [
        {
          "name": "_liquidity",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeGrowthInside0LastX128",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeGrowthInside1LastX128",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tokensOwed0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tokensOwed1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "slot0",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "sqrtPriceX96",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tick",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "observationIndex",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "observationCardinality",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "observationCardinalityNext",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeProtocol",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "unlocked",
          "type": "bool",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bool"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "tickBitmap",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "wordPosition",
          "type": "int16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": [
        {
          "name": "",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "ticks",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "tick",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": [
        {
          "name": "liquidityGross",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "liquidityNet",
          "type": "int128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "feeGrowthOutside0X128",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeGrowthOutside1X128",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tickCumulativeOutside",
          "type": "int56",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "secondsPerLiquidityOutsideX128",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "secondsOutside",
          "type": "uint32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "initialized",
          "type": "bool",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bool"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "feeGrowthGlobal1X128",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "protocolFees",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "token0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "token1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    },
    {
      "type": "function",
      "name": "feeGrowthGlobal0X128",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "setFeeProtocol",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "feeProtocol0",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeProtocol1",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "slot0",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "sqrtPriceX96",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tick",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "observationIndex",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "observationCardinality",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "observationCardinalityNext",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeProtocol",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "unlocked",
          "type": "bool",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bool"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "snapshotCumulativesInside",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": [
        {
          "name": "tickCumulativeInside",
          "type": "int56",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "secondsPerLiquidityInsideX128",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "secondsInside",
          "type": "uint32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "token1",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "collectProtocol",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "amount0Requested",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1Requested",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "amount0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "fee",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "feeGrowthGlobal1X128",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "initialize",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "sqrtPriceX96",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "liquidity",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "observations",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "index",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "blockTimestamp",
          "type": "uint32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tickCumulative",
          "type": "int56",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "secondsPerLiquidityCumulativeX128",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "initialized",
          "type": "bool",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bool"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "observe",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "secondsAgos",
          "type": "uint32[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "uint"
            }
          }
        }
      ],
      "outputs": [
        {
          "name": "tickCumulatives",
          "type": "int56[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "int"
            }
          }
        },
        {
          "name": "secondsPerLiquidityCumulativeX128s",
          "type": "uint160[]",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "slice",
            "nested_type": {
              "type": "uint"
            }
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "positions",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "key",
          "type": "bytes32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ],
      "outputs": [
        {
          "name": "_liquidity",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeGrowthInside0LastX128",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeGrowthInside1LastX128",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tokensOwed0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tokensOwed1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "increaseObservationCardinalityNext",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "observationCardinalityNext",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "maxLiquidityPerTick",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "tickBitmap",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "wordPosition",
          "type": "int16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": [
        {
          "name": "",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "tickSpacing",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "ticks",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [
        {
          "name": "tick",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": [
        {
          "name": "liquidityGross",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "liquidityNet",
          "type": "int128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "feeGrowthOutside0X128",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeGrowthOutside1X128",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tickCumulativeOutside",
          "type": "int56",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "secondsPerLiquidityOutsideX128",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "secondsOutside",
          "type": "uint32",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "initialized",
          "type": "bool",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bool"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "token0",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "collect",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount0Requested",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1Requested",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "amount0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "factory",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "flash",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "data",
          "type": "bytes",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ],
      "outputs": []
    },
    {
      "type": "function",
      "name": "mint",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "data",
          "type": "bytes",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ],
      "outputs": [
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "protocolFees",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "token0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "token1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "swap",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "zeroForOne",
          "type": "bool",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bool"
          }
        },
        {
          "name": "amountSpecified",
          "type": "int256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "sqrtPriceLimitX96",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "data",
          "type": "bytes",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "bytes"
          }
        }
      ],
      "outputs": [
        {
          "name": "amount0",
          "type": "int256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount1",
          "type": "int256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "burn",
      "constant": false,
      "anonymous": false,
      "stateMutability": "nonpayable",
      "inputs": [
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": [
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "event",
      "name": "Burn",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "owner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "Collect",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "owner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "CollectProtocol",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "sender",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "amount0",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "IncreaseObservationCardinalityNext",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "observationCardinalityNextOld",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "observationCardinalityNextNew",
          "type": "uint16",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "Initialize",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "sqrtPriceX96",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tick",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "Mint",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "sender",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "owner",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "tickLower",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "tickUpper",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "SetFeeProtocol",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "feeProtocol0Old",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeProtocol1Old",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeProtocol0New",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "feeProtocol1New",
          "type": "uint8",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "Flash",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "sender",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "amount0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "amount1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "paid0",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "paid1",
          "type": "uint256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ],
      "outputs": null
    },
    {
      "type": "event",
      "name": "Swap",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": [
        {
          "name": "sender",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "recipient",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": true,
          "simple_type": {
            "type": "address"
          }
        },
        {
          "name": "amount0",
          "type": "int256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "amount1",
          "type": "int256",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        },
        {
          "name": "sqrtPriceX96",
          "type": "uint160",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "liquidity",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        },
        {
          "name": "tick",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ],
      "outputs": null
    }
  ],
  [
    {
      "type": "constructor",
      "name": "",
      "constant": false,
      "anonymous": false,
      "stateMutability": "",
      "inputs": null,
      "outputs": null
    },
    {
      "type": "function",
      "name": "fee",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "uint24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "maxLiquidityPerTick",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "uint128",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "uint"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "tickSpacing",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "int24",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "int"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "token0",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "token1",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    },
    {
      "type": "function",
      "name": "factory",
      "constant": false,
      "anonymous": false,
      "stateMutability": "view",
      "inputs": [],
      "outputs": [
        {
          "name": "",
          "type": "address",
          "storage_location": "default",
          "offset": 0,
          "index": "0x0000000000000000000000000000000000000000000000000000000000000000",
          "indexed": false,
          "simple_type": {
            "type": "address"
          }
        }
      ]
    }
  ]
]
""")