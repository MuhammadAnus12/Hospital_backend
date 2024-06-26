from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base, engine
from sqlalchemy.orm import relationship

class Appointment(Base):
    __tablename__ = 'Appointment'
    id = Column(Integer, primary_key=True, index=True)
    patient_id=Column(Integer, ForeignKey('Patient.id'))
    doctor_id=Column(Integer, ForeignKey('Doctor.id'))
    appointment_date=Column(Date, nullable=False)
    appointment_time=Column(String, nullable=False)
    status=Column(String, nullable=False)

    patient=relationship("Patient", back_populates="appointments")
    doctor=relationship("Doctor", back_populates="appointments")

