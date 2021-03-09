from typing import Optional, List, Dict, Any
from fastapi import FastAPI
from app.models.modelo import Item, ItemResposta
from app.server.data import ListaDesejos, StatusItens


app = FastAPI()

wishlist = ListaDesejos()
# class User(BaseModel):

#     id: str

#     name: str

#     email: str


# @app.get("/users/{user_id}")
# def listar_usuarios(item_id: int, q: Optional[str] = None):
#     """
#         Cadastra usuários
#     """
#     return {"item_id": item_id, "q": q}

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bem Vindo a Lista de Desejos! - Acrescente '/docs' ao final da URL para acessar a documentação"}


@app.get("/wishlist", response_model=List[ItemResposta])
def filtrar_itens_nao_possuidos(have: Optional[StatusItens] = None):
    """
        retorna lista de desejos que ainda não foram adquiridos
    """
    if have is not None:
        return wishlist.filtrar(have=have)
    return wishlist.listar()


@app.post("/wishlist", response_model=ItemResposta, status_code=201)
def inserir_wishlist(item_a_inserir: Item):
    """
        insere um item na lista de desejos
    """
    return wishlist.inserir(item_a_inserir.dict())


@app.get("/wishlist/{item_id}", response_model=ItemResposta, status_code=201)
def filtrar_wishlist(id_do_item: int):
    """
        view que mostra o item de desejo a partir do id dele
    """
    return wishlist.pegar(id_do_item)


@app.get("/wishlist", response_model=List[ItemResposta])
def filtrar_itens(have: Optional[StatusItens] = None):
    """
        Realiza o filtro na lista de desejos (WishList) e retorna os itens de acordo com a opção escolhida.\n
        Opção --- : realiza o filtro na lista completa\n
        Opção False: Retorna os itens ainda não adquiridos\n
        Opção True: Retorna os itens já comprados / ganhos
    """
    if have is not None:
        return wishlist.filtrar(have=have)
    return wishlist.listar()


# @app.put("/wishlist")
# def update_item(item_id: int, item: Item):
#     """
#         Atualiza desejo se o usuário já possui
#     """

#     return {"item_have": item.have, "item_id": item_id}
