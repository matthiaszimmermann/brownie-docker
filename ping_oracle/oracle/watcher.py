import logging

from threading import Thread
from time import sleep
from typing import List

from oracle.event import Event
from oracle.player import PlayerContract

# implementation informed by 
# https://cryptomarketpool.com/how-to-listen-for-ethereum-events-using-web3-in-python/
class PlayerWatcher(object):

    def __init__(self, player:PlayerContract, events:List[Event]):
        self._player = player
        self._events = events
        self.active = True

    def start(self):
        contract = self._player.w3contract
        logMoveFilter = contract.events.LogMove.createFilter(
            fromBlock='latest')

        worker = Thread(
            target=self._eventLoop, 
            args=(logMoveFilter, 1), 
            daemon=True)
    
        worker.start()

    def _eventLoop(self, eventFilter, pollingIntervall):
        while self.active:
            for event in eventFilter.get_new_entries():
                self._handleEvent(event)
        
            sleep(pollingIntervall)

    def _handleEvent(self, event):
        evt = Event(
            id = '({},{},{})'.format(
                event.blockNumber,
                event.transactionIndex,
                event.logIndex),
            address = event.address,
            event = event.event,
            args = dict(event.args))
        
        self._events.append(evt)
        logging.info(evt)
