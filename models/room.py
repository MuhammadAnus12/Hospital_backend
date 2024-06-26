from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Room(Base):
    __tablename__ = 'Room'
    id = Column(Integer, primary_key=True, index=True)
    number= Column(Integer, nullable=False)
    type = Column(String, nullable=False)
    availability_status=Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('Department.id'))
    
    doctors = relationship('Doctor', back_populates='room')
    department = relationship('Department', back_populates='rooms')
    equipment = relationship('Equipment', back_populates='room')
