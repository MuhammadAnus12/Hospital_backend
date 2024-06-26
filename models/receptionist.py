from sqlalchemy import Column, Integer, String
from database import Base, engine

class Receptionist(Base):
    __tablename__ = 'Receptionist'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    phone_number = Column(String,nullable=False)
    email = Column(String,nullable=False)
    shift=Column(String,nullable=False)
