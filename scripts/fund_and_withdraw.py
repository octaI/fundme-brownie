from brownie import FundMe

from scripts.utils import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f" Current entrance fee: {entrance_fee}")
    print(f"Funding..")
    fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    print("Funds withdrawn.")

def main():
    fund()
    withdraw()