import logging

from threading import Thread
from time import sleep
from typing import List

from brownie import network
from brownie.network.contract import Contract
from brownie.network.web3 import web3

# setup to allow importing smart contract class Player
from brownie import project
p = project.load('.', name="Project")
p.load_config()
from brownie.project.Project import Player

from oracle.account import Account
from oracle.event import Event

# implementation informed by 
# https://cryptomarketpool.com/how-to-listen-for-ethereum-events-using-web3-in-python/
class PlayerContract(object):

    NETWORK_NAME = 'ganache'

    def __init__(self, address:str, networkName=NETWORK_NAME):
        if not network.is_connected():
            network.connect(networkName)

        self._contract = Contract.from_abi(
            Player._name, 
            address, 
            Player.abi,
            persist = False)

        self._w3contract = web3.eth.contract(
            address, abi=Player.abi)

    @property
    def address(self) -> str:
        return self._contract.address

    @property
    def contract(self) -> Player:
        return self._contract

    @property
    def w3contract(self):
        return self._w3contract
    
    def move(self, calls:int, account: Account):
        acct = account.brownieAccount
        self._contract.move(calls, {'from': acct})
