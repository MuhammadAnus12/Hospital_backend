from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Ward(Base):
    __tablename__ = 'Ward'
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String, nullable=False)
    type = Column(String, nullable=False)
    capacity=Column(Integer, nullable=False)