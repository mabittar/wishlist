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
    return "Insira \docs para ver a documentação completa"


@app.get("/wishlist", response_model=List[schemas.Wish])
async def lista_desejos(have: Optional[bool] = None, db: Session = Depends(get_db)):
    return crud.list_wishes_filter(db, have)


@app.get("/wishlist/{id}", response_model=schemas.Wish)
async def filtra_id(id: int, db: Session = Depends(get_db)):
    wish_db = crud.get_wish(db, id)
    if wish_db:
        return wish_db
    raise HTTPException(
        status_code=404, detail="ID não encontrado / ID not found")


@app.post("/wishlist", response_model=schemas.Wish)
async def criar_novo_desejo(desejo: schemas.WishCreate, db: Session = Depends(get_db)):
    return crud.create_wish(db, desejo)
