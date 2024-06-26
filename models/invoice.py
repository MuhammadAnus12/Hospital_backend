from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship

class Invoice(Base):
    __tablename__ = 'Invoice'
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey('Patient.id'))
    invoice_date = Column(Date, nullable=False)
    amount = Column(Integer, nullable=False)
    payment_status = Column(String, nullable=False)

    patient = relationship("Patient", back_populates="invoices")
    payments = relationship("Payment", back_populates="invoice")
    

