import pytest
from brownie import network, accounts, exceptions

from scripts.utils import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fundme

def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fundme()
    entrance_fee = fund_me.getEntranceFee() + 1000
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx = fund_me.withdraw({"from": account})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only local testing")
    account = get_account()
    fund_me = deploy_fundme()
    other_acc = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": other_acc})