from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Nurse(Base):
    __tablename__ = 'Nurse'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)
    shift = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('Department.id'))

    department = relationship("Department", back_populates="nurses")
