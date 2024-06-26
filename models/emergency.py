from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship

class Emergency(Base):
    __tablename__ = 'Emergency'
    id = Column(Integer, primary_key=True, index=True)
    contact_name = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    relationships = Column(String, nullable=False)

    patient = relationship("Patient", back_populates="emergency")
    
    