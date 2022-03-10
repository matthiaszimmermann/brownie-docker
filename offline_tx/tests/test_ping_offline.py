# brownie web3 directly inherits from web3 python lib
# see https://github.com/eth-brownie/brownie/blob/master/brownie/network/web3.py
from brownie import (
    web3,
    Wei,
)

from scripts.util import (
    get_web3_contract,
    get_signed_transaction,
    submit_signed_transaction,
)

def test_ping_offline(pingContract, owner, accounts):
    test_number = 42

    # create web3 instance for pingContract
    w3ping = get_web3_contract(pingContract)
    
    # create offline signed tx for owner to call the ping method
    # create raw tx (without nonce)
    tx_raw = w3ping.functions.ping(test_number).buildTransaction()

    # sign transaction with owner private key and submit
    tx_raw_signed = get_signed_transaction(tx_raw, owner)
    tx_sent = submit_signed_transaction(tx_raw_signed)

    assert pingContract.pings({'from': accounts[0]}) == 1
    assert pingContract.pingSum({'from': accounts[0]}) == test_number

def test_ping_offline_w_funds_transfer(pingContract, owner, accounts):
    test_number = 17
    test_amount = Wei('0.5 ether');

    assert pingContract.pings({'from': accounts[0]}) == 0
    assert pingContract.pingSum({'from': accounts[0]}) == 0
    assert pingContract.balance() == 0

    # create web3 instance for pingContract
    w3ping = get_web3_contract(pingContract)
    
    # create offline signed tx for owner to call the ping method
    # create raw tx (without nonce)
    tx_raw = w3ping.functions.ping(test_number).buildTransaction()

    # sign transaction with owner private key and submit
    tx_raw_signed = get_signed_transaction(
        tx_raw, 
        owner, 
        nonce=owner.nonce,
        value=test_amount)
    
    tx_sent = submit_signed_transaction(tx_raw_signed)

    assert pingContract.pings({'from': accounts[0]}) == 1
    assert pingContract.pingSum({'from': accounts[0]}) == test_number
    assert pingContract.balance() == test_amount
