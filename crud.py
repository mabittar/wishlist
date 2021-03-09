from sqlalchemy.orm import Session
import models
import schemas


def list_wishes_filter(db: Session, have: bool = None):
    if have is not None:
        return db.query(models.Wish).filter(models.Wish.have == have).all()
    return db.query(models.Wish).all()


def create_wish(db: Session, wish: schemas.WishCreate):
    wish_db = models.Wish(**wish.dict())
    # wish_db = models.Wish(name=wish.name, description=wish.description...)
    db.add(wish_db)
    db.commit()
    db.refresh(wish_db)
    return wish_db


def get_wish(db: Session, wish_id: int):
    return db.query(models.Wish).filter(models.Wish.id == wish_id).first()
