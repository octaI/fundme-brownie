# fundme-brownie

This repo contains an implementation of a simple Fund Me contract, and Brownie scripts to deploy and interact with it.

## Usage
1. Create a .env file containing the following exports:

`export PRIVATE_KEY=<Your wallet Private Key>`

2. `brownie compile` 
3. `brownie run scripts/deploy.py` to deploy. You can specify different networks with `--network` flag
4. `brownie run scripts/fund_and_withdraw` to interact with the smart contract.
