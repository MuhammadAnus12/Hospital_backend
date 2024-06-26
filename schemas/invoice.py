from pydantic import BaseModel
from datetime import date
from typing import List

class InvoiceBase(BaseModel):
    patient_id: int
    invoice_date: date
    amount: int
    payment_status: str

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceUpdate(InvoiceBase):
    id: int

class Invoice(InvoiceBase):
    id: int

    class ConfigDict:
        from_attributes = True

class Invoices(BaseModel):
    invoices: List[Invoice]
    total_count: int
        