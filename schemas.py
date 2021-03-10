from pydantic import BaseModel
from typing import Optional, List


class WishBase(BaseModel):
    name: str
    description: Optional[str]
    image_link: Optional[str]
    link: Optional[str]
    have: bool = False


class WishCreate(WishBase):
    ...


class WishUpdate(WishBase):
    name: Optional[str]
    description: Optional[str]
    image_link: Optional[str]
    link: Optional[str]
    have: bool = True


class Wish(WishBase):
    id: int

    class Config:
        orm_mode = True
