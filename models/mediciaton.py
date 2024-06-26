from sqlalchemy import Column, Integer, String, ForeignKey,Date
from database import Base
from sqlalchemy.orm import relationship

class Mediciation(Base):
    __tablename__ = 'Mediciation'
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String, nullable=False)
    manufacturer=Column(String, nullable=False)
    expiry_date=Column(Date, nullable=False)
    quantity_in_stock=Column(Integer, nullable=False)
    price=Column(Integer, nullable=False)

    prescriptions = relationship('Prescription', back_populates='medication')



    
