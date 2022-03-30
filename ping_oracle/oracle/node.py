import logging

from typing import Dict, List

from oracle.account import Account
from oracle.event import Event
from oracle.player import PlayerContract
from oracle.watcher import PlayerWatcher

class Node(object):

    def __init__(self):
        self._players:Dict[str, PlayerContract] = {}
        self._events:List[Event] = []
        self._account = Account()

    @property
    def events(self) -> List[Event]:
        return self._events
    
    @property
    def players(self) -> List[str]:
        return list(self._players.keys())
    
    @players.setter
    def players(self, playerAddresses: List[str]):
        for address in playerAddresses:
            # create player and add it to known players
            player = PlayerContract(address)
            self._players[address] = player

            # create and start watcher for on-chain events  
            watcher = PlayerWatcher(player, self._events)
            watcher.start()

    def move(self, address:str, calls:int):
        if not address in self._players.keys():
            raise ValueError('unknown player address {}'.format(address))

        # tigger move transaction for player contract
        player = self._players[address]
        player.move(calls, self._account)
