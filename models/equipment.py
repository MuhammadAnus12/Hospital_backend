from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship

class Equipment(Base):
    __tablename__ = 'Equipment'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    purchase_date = Column(Date, nullable=False)
    maintenance_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    room_id = Column(Integer, ForeignKey('Room.id'))

    room=relationship("Room", back_populates="equipment")
