from sqlalchemy import Column, Integer, String
from database import Base

class Supplier(Base):
    __tablename__ = 'Supplier'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact_person = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    address = Column(String, nullable=False)

