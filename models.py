from sqlalchemy import String, Column, Integer
from database import Base

class Persons(Base):
    __tablename__="persons"

    id = Column(Integer, primary_key=True, index=False)
    name = Column(String, index=False)