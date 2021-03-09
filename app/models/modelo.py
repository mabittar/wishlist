from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from app.server.data import StatusItens


class Item(BaseModel):
    name: str = Field(...)
    description: Optional[str]
    image: Optional[str]
    link: Optional[str]
    have: StatusItens

    class Config:
        schema_extra = {
            "exemplo": {
                "name": "Mouse pad",
                "description": "Mouse pad de grandes dimensoes",
                "image": "",
                "link": "",
                "have": False

            }
        }


class ItemResposta(Item):
    id: int


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}