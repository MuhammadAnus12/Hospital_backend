from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base, engine
from sqlalchemy.orm import relationship

class Patient(Base):
    __tablename__ = 'Patient'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    date_of_birth =Column(Date,nullable=False)
    gender = Column(String,nullable=False)
    address = Column(String,nullable=False)    
    phone_number = Column(String,nullable=False)
    email = Column(String,nullable=False)
    emergency_id = Column(Integer, ForeignKey('Emergency.id'))
    insurance_id = Column(Integer, ForeignKey('Insurance.id'))
    medical_record_id = Column(Integer, ForeignKey('MedicalRecord.id'))

    emergency = relationship("Emergency", back_populates="patient")
    insurance = relationship("Insurance", back_populates="patient")
    medical_record = relationship("MedicalRecord", back_populates="patient")
    appointments = relationship("Appointment", back_populates="patient")
    treatments = relationship("Treatment", back_populates="patient")
    labtests = relationship("LabTest", back_populates="patient")
    invoices = relationship("Invoice", back_populates="patient")


    

    
    
