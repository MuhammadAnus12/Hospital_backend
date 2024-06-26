from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship




class Doctor(Base):
    __tablename__ = 'Doctor'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    room_id = Column(Integer, ForeignKey('Room.id'))
    department_id = Column(Integer, ForeignKey('Department.id'))

    departments=relationship('DoctorDepartment', back_populates='doctor')
    room = relationship('Room', back_populates='doctors')
    appointments=relationship('Appointment', back_populates='doctor')
    treatments=relationship('Treatment', back_populates='doctor')
    
