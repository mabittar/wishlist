from sqlalchemy.orm import Session
from sqlalchemy.sql import func
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


def delete_wish(db: Session, wish_id: int):
    db.query(models.Wish).filter(models.Wish.id == wish_id).delete()
    db.commit()


def update_wish(db: Session, wish_id: int, wish: schemas.WishUpdate):
    wish_db = get_wish(db, wish_id)
    wish_db.wish = wish.have or wish_db.have
    wish_db.image_link = wish.image_link or wish_db.image_link
    wish_db.link = wish.link or wish_db.link
    wish_db.description = wish.description or wish_db.description

    db.add(wish_db)
    db.commit()
    db.refresh(wish_db)
    return wish_db


def randon_wishes_filter(db: Session, have=False):
    wish_rand = db.query(models.Wish).filter(
        models.Wish.have == have).all().func.random()
    return wish_rand
