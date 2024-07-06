from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Department(Base):
    __tablename__ = 'Department'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    doctors = relationship('Doctor', back_populates='department')
    nurses = relationship('Nurse', back_populates='department')
    rooms = relationship('Room', back_populates='department')
    headofdepartment=relationship('HeadOfDepartment',back_populates='department')
