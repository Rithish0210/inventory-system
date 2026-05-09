from sqlalchemy import Column, Integer, String, Float
from database.db import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    unit = Column(String)
    quantity = Column(Float)
    threshold = Column(Float)

Base.metadata.create_all(bind=engine)