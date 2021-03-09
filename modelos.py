from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from data import StatusItens


class Item(BaseModel):
    name: str
    description: Optional[str]
    image: Optional[str]
    link: Optional[str]
    have: StatusItens


class ItemResposta(Item):
    id: int
