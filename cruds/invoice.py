from sqlalchemy.orm import Session
from models import invoice as model_invoice
from schemas import invoice as schema_invoice
from typing import List


def create_invoice(db: Session, invoice: schema_invoice.InvoiceCreate):
    db_invoice = model_invoice.Invoice(**invoice.dict())
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_invoice.Invoice).offset(skip).limit(limit).all()

def get_invoice(db: Session, invoice_id: int):
    db_invoice = db.query(model_invoice.Invoice).filter(
        model_invoice.Invoice.id == invoice_id).first()
    if db_invoice is None:
        return None
    return db_invoice

def update_invoice(db: Session, invoice: schema_invoice.InvoiceUpdate):
    db_invoice = db.query(model_invoice.Invoice).filter(
        model_invoice.Invoice.id == invoice.id).first()
    if db_invoice is None:
        return None
    for key, value in invoice.dict().items():
        setattr(db_invoice, key, value)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def delete_invoice(db: Session, invoice_id: int):
    db_invoice = db.query(model_invoice.Invoice).filter(
        model_invoice.Invoice.id == invoice_id).first()
    if db_invoice is None:
        return None
    db.delete(db_invoice)
    db.commit()
    return db_invoice