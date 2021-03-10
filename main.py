from pydantic import BaseModel
from typing import Optional, List, Dict, Any
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


@app.get("/")
async def root():
    return "Insira /docs para ver a documentação completa"


@app.get("/wishlist", response_model=List[schemas.Wish])
async def lista_desejos(have: Optional[bool] = None, db: Session = Depends(get_db)):
    '''Endlist para a lista de Desejos '''
    return crud.list_wishes_filter(db, have)


@app.get("/wishlist/{id}", response_model=schemas.Wish)
async def filtra_id(id: int, db: Session = Depends(get_db)):
    '''Filtra a lista de desejos pelo ID '''
    wish_db = crud.get_wish(db, id)
    if wish_db:
        return wish_db
    raise HTTPException(
        status_code=404, detail="ID não encontrado / ID not found")


@app.post("/wishlist", response_model=schemas.Wish, status_code=201)
async def criar_novo_desejo(desejo: schemas.WishCreate, db: Session = Depends(get_db)):
    '''Cria um novo desejo.\n
    Os campos descrição, image_link e link são opcionais
    No campo name deve ser informado o nome do desejo
    No campo have deve ser informado se o usuário já possui (True or False)
     '''
    return crud.create_wish(db, desejo)

# TODO: otimizar a busca pelo banco


@app.delete("/wishlist/{id}", status_code=204)
async def deletar_desejo(id: int, db: Session = Depends(get_db)):
    '''Delata desejo a partir do ID '''
    wish_db = crud.get_wish(db, id)
    if wish_db is not None:
        crud.delete_wish(db, id)
        return "Desejo removido"
    raise HTTPException(
        status_code=404, detail="ID não encontrado / ID not found")


@app.patch("/wishlist/{id}", response_model=schemas.Wish)
async def atualiza_desejo(id: int, desejo: schemas.WishUpdate, db: Session = Depends(get_db)):
    '''Atualiza o campo have para indicar se o usuário já possui / comprou tal desejo '''
    wish_db = crud.get_wish(db, id)
    if wish_db:
        return crud.update_wish(db, id, desejo)
    raise HTTPException(
        status_code=404, detail="ID não encontrado / ID not found")
