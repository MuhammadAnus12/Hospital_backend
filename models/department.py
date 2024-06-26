from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class DoctorDepartment(Base):
    __tablename__ = 'DoctorDepartment'
    id=Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey('Doctor.id'), primary_key=True)
    department_id = Column(Integer, ForeignKey('Department.id'), primary_key=True)

    doctor = relationship('Doctor', back_populates='departments')
    department = relationship('Department', back_populates='doctors')


class Department(Base):
    __tablename__ = 'Department'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    nurses = relationship('Nurse', back_populates='department')
    doctors = relationship('DoctorDepartment', back_populates='department')
    rooms = relationship('Room', back_populates='department')

