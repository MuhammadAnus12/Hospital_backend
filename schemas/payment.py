from pydantic import BaseModel
from datetime import date
from typing import List

class PaymentBase(BaseModel):
    invoice_id: int
    date: date
    amount: int
    method: str

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(PaymentBase):
    id: int

class Payment(PaymentBase):
    id: int
    class ConfigDict:
        from_attributes = True

class PaymentID(Payment):
    id: int
    class ConfigDict:
        from_attributes = True

class Payments(BaseModel):
    payments: List[Payment]
    total_count: int