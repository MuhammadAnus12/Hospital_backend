from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class HeadOfDepartment(Base):
    __tablename__="HeadOfDepartment"
    id=Column(Integer,primary_key=True,index=True)
    doctor_id=Column(Integer,ForeignKey('Doctor.id'))
    department_id=Column(Integer,ForeignKey('Department.id'))
    name=Column(String,nullable=False)

    doctor=relationship('Doctor',back_populates='headofdepartment')
    department=relationship('Department',back_populates='headofdepartment')