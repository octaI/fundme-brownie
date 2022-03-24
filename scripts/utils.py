from brownie import network, accounts, config, MockV3Aggregator

# Constants
DECIMALS = 8
STARTING_PRICE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local-octa"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]


def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS + FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    print(f"Current network: {network.show_active()}")
    print("Deploying mock...")
    if len(MockV3Aggregator) < 1:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mock deployed")