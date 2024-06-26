from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship

class Insurance(Base):
    __tablename__ = 'Insurance'
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    policy_number = Column(Integer, nullable=False)
    coverage_details = Column(String, nullable=False)


    patient= relationship("Patient", back_populates="insurance")

    
