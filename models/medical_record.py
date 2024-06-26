from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship

class MedicalRecord(Base):
    __tablename__ = 'MedicalRecord'
    id = Column(Integer, primary_key=True, index=True)
    details = Column(String, nullable=False)
    created_date = Column(Date, nullable=False)

    patient = relationship("Patient", back_populates="medical_record")
