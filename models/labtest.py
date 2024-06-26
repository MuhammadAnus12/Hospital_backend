from sqlalchemy import Column, Integer, String, ForeignKey,Date
from database import Base
from sqlalchemy.orm import relationship


class LabTest(Base):
    __tablename__ = 'LabTest'
    id = Column(Integer, primary_key=True, index=True)
    patient_id=Column(Integer, ForeignKey('Patient.id'))
    lab_technician_id=Column(Integer, ForeignKey('LabTechnician.id'))
    test_name=Column(String, nullable=False)
    test_date=Column(Date, nullable=False)
    result=Column(String, nullable=False)

    patient = relationship("Patient", back_populates="labtests")
    labtechnician = relationship("LabTechnician", back_populates="labtests")

