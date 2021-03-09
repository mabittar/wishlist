from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class WishBase(BaseModel):
    name: str
    description: Optional[str]
    image_link: Optional[str]
    link: Optional[str]
    have: bool


class WishCreate(WishBase):
    ...


class Wish(WishBase):
    id: int

    class Config:
        orm_mode = True