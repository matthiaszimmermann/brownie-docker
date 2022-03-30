from typing import Dict
from pydantic import BaseModel

class Event(BaseModel):
    id: str = None
    address: str = None
    event: str = None
    args: Dict = None
