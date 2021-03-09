from typing import Optional, List, Dict, Any, Union
from enum import Enum


class StatusItens(str, Enum):
    nao_possui = False
    possui = True


Item = Dict[str, Union[int, str, StatusItens]]


class ListaDesejos():
    wishlist: List[Item] = [
        {"id": 1, "name": "Notebook", "description": "notebook portátil",
            "image": None, "link": "", "have": StatusItens.possui},
        {"id": 2, "name": "Computador", "description": "computador de mesa",
            "image": None, "link": "", "have": StatusItens.nao_possui}
    ]
    id_atual = 2

    def listar(self):
        return self.wishlist

    def inserir(self, item: Item) -> Item:
        self.id_atual += 1
        item["id"] = self.id_atual
        self.wishlist.append(item)
        return item

    def pegar(self, item_id: int) -> Item:
        item = filter(lambda x: x["id"] == item_id, self.wishlist)
        return list(item)[0]

    def filtrar(self, have: StatusItens) -> List[Item]:
        return list(filter(lambda x: x["have"] == have, self.wishlist))
