from pydantic import BaseModel
from typing import Optional


WISHES = []

fake_wish_db = {
    # hashed_password == secret
    "presenta A": {
        "name": "mouse",
        "description": "mouse sem fio",
        "image_link": "https://www.corsair.com/corsairmedia/sys_master/productcontent/ch-9315311-na-dark_core_rgb_se_04.png",
        "link": "https://www.corsair.com/br/pt/Categorias/Produtos/Mouses-gamer/Wireless-Gaming-Mice/DARK-CORE-RGB-PRO-SE-Wireless-Gaming-Mouse/p/CH-9315511-NA",
        "have": False,
    }
}


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
