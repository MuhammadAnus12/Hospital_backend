from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Prescription(Base):
    __tablename__ = 'Prescription'
    id = Column(Integer, primary_key=True, index=True)
    treatment_id=Column(Integer, ForeignKey('Treatment.id'))
    medication_id=Column(Integer, ForeignKey('Mediciation.id'))
    dosage=Column(String, nullable=False)
    frequency=Column(String, nullable=False)
    duration=Column(String, nullable=False)

    treatment = relationship('Treatment', back_populates='prescriptions')
    medication = relationship('Mediciation', back_populates='prescriptions')