from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class LabTechnician(Base):
    __tablename__ = 'LabTechnician'
    id = Column(Integer, primary_key=True, index=True)
    first_name=Column(String, nullable=False)
    last_name=Column(String, nullable=False)
    email=Column(String, nullable=False)
    phone_number=Column(String, nullable=False)

    labtests = relationship("LabTest", back_populates="labtechnician")