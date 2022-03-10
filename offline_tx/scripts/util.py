from typing import Dict

from brownie import (
    web3,
    network, 
    accounts, 
)

# brownie Web3 directly inherits from Web3.py
from brownie.network.web3 import Web3 
from brownie.network.account import Account

from scripts.const import (
    NETWORKS_DEV,
    MNEMONIC_DEV,
    NETWORKS,
    MNEMONIC,
)

def get_web3() -> Web3:
    return web3

def get_owner_account() -> Account:
    if network.show_active() in NETWORKS_DEV:
        return accounts.from_mnemonic(MNEMONIC_DEV, count=1, offset=0)
    elif network.show_active() in NETWORKS:
        return accounts.from_mnemonic(MNEMONIC, count=1, offset=0)

    return None

def get_web3_contract(brownieContract):
    return web3.eth.contract(
        address=brownieContract.address, 
        abi=brownieContract.abi)

def get_signed_transaction(
    raw_transaction: Dict, 
    account: Account, 
    nonce: int = -1,
    value: int = 0,
):
    # set nonce value to use for tx
    if nonce < 0:
        raw_transaction['nonce'] = account.nonce
    else:
        raw_transaction['nonce'] = nonce

    # set amount value to use for tx (only if value > 0)
    if value > 0:
        raw_transaction['value'] = value

    return web3.eth.account.sign_transaction(
        raw_transaction, 
        account.private_key)

def submit_signed_transaction(signed_transaction):
    return web3.eth.send_raw_transaction(signed_transaction.rawTransaction)