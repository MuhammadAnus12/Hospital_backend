from sqlalchemy import Column, Integer, String, ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship

class Payment(Base):
    __tablename__ = 'Payment'
    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey('Invoice.id'))
    date = Column(Date, nullable=False)
    amount = Column(Integer, nullable=False)
    method = Column(String, nullable=False)

    invoice= relationship("Invoice", back_populates="payments")
