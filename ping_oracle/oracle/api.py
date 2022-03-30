
from fastapi import FastAPI, HTTPException
from typing import List

from oracle.event import Event
from oracle.node import Node

import logging
logging.getLogger().setLevel(logging.INFO)

app = FastAPI()
node = Node()

@app.get('/events', response_model=List[Event])
def get_events():
    global node
    return node.events

@app.get('/players', response_model=List[str])
def get_players():
    global node
    return node.players

@app.post('/players')
def set_players(addresses: List[str]):
    global node
    node.players = addresses

@app.post('/players/{address}/move')
def player_move(address:str, calls:int):
    try:
        global node
        node.move(address, calls)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
