from sqlalchemy import Column, String, Integer, Boolean
from database import Base

class Wish(Base):
    __tablename__  = 'Wishes'

    id = Column(Integer, primary_key=True)

    name = Column(String(50))

    description = Column(String(75))

    image_link = Column(String, nullable=True)

    link = Column(String, nullable=True)

    have = Column(Boolean)