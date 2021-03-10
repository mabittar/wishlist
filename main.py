from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends
from database import engine, SessionLocal
from sqlalchemy.orm import Session
import schemas
import models
import crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["Roots"])
async def index():
    return {"message": "Insira /docs para ver a documentação completa"}


@app.get("/wishlist", response_model=List[schemas.Wish], tags=["Wishlist"])
async def lista_desejos(have: Optional[bool] = None, db: Session = Depends(get_db)):
    '''Endpoint para a lista de Desejos '''
    return crud.list_wishes_filter(db, have)


@app.get("/wishlist/{id}", response_model=schemas.Wish, tags=["Wishlist"])
async def filtra_id(id: int, db: Session = Depends(get_db)):
    '''Filtra a lista de desejos pelo ID '''
    wish_db = crud.get_wish(db, id)
    if wish_db:
        return wish_db
    raise HTTPException(
        status_code=404, detail="ID não encontrado / ID not found")


@app.post("/wishlist", response_model=schemas.Wish, status_code=201, tags=["Wishlist"])
async def criar_novo_desejo(desejo: schemas.WishCreate, db: Session = Depends(get_db)):
    '''Cria um novo desejo.\n
    Os campos descrição, image_link e link são opcionais\n
    No campo name deve ser informado o nome do desejo\n
    No campo have deve ser informado se o usuário já possui (True or False)
     '''
    return crud.create_wish(db, desejo)

# TODO: otimizar a busca pelo banco


@app.delete("/wishlist/{id}", status_code=204, tags=["Wishlist"])
async def deletar_desejo(id: int, db: Session = Depends(get_db)):
    '''Delata desejo a partir do ID '''
    wish_db = crud.get_wish(db, id)
    if wish_db is not None:
        crud.delete_wish(db, id)
        return "Desejo removido"
    raise HTTPException(
        status_code=404, detail="ID não encontrado / ID not found")


@app.patch("/wishlist/{id}", response_model=schemas.Wish, tags=["Wishlist"])
async def atualiza_desejo_pelo_ID(id: int, desejo: schemas.WishUpdate, db: Session = Depends(get_db)):
    '''Atualiza os campos\n
    have para indicar se o usuário já possui / comprou tal desejo\n
    as demais informações também podem ser altaradas, com exceção do campo name'''
    wish_db = crud.get_wish(db, id)
    if wish_db:
        return crud.update_wish(db, id, desejo)
    raise HTTPException(
        status_code=404, detail="ID não encontrado / ID not found")


@app.get("/wishlist/?have=false", response_model=List[schemas.Wish], tags=["Busca Randômica"])
async def lista_desejos_aleatorio(have=False, db: Session = Depends(get_db)):
    '''Endpoint para realizar uma busca na lista de desejos\n
    returna um desejo aleatório. '''
    return crud.randon_wishes_filter(db, have)
