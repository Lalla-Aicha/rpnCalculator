from sqlalchemy import Column, Integer, Float, String
from database import Base

class Operation(Base):
    __tablename__ = "operations"
    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String, index=True)
    result = Column(Float)