from sqlalchemy import Column, Integer, String, Float
from .db import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    category = Column(String, index=True)
    location = Column(String)
    price = Column(Float)
    area = Column(Float)
    rooms = Column(Integer)
    description = Column(String)
    photos = Column(String)
