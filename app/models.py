from sqlalchemy import Column, String, Integer, Boolean
from app.database import Base


class Wish(Base):
    __tablename__ = 'Wishes'

    id = Column(Integer, primary_key=True)

    name = Column(String(50))

    description = Column(String(75), nullable=True)

    image_link = Column(String, nullable=True)

    link = Column(String, nullable=True)

    have = Column(Boolean, default=False)
