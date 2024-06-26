from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship

class Treatment(Base):
    __tablename__ = 'Treatment'
    id = Column(Integer, primary_key=True, index=True)
    patient_id=Column(Integer, ForeignKey('Patient.id'))
    doctor_id=Column(Integer, ForeignKey('Doctor.id'))
    diagnosis=Column(String, nullable=False)
    treatment_plan=Column(String, nullable=False)
    start_date=Column(Date, nullable=False)
    end_date=Column(Date, nullable=False)

    patient = relationship('Patient', back_populates='treatments')
    doctor = relationship('Doctor', back_populates='treatments')
    prescriptions = relationship('Prescription', back_populates='treatment')