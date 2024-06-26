from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import invoice as model_invoice
from cruds import invoice as crud_invoice
from schemas import invoice as schema_invoice


router = APIRouter()
tags = ["Invoice"]

@router.post("/invoice", response_model=schema_invoice.Invoice, tags=tags)
def create_invoice(invoice: schema_invoice.InvoiceCreate, db: Session = Depends(get_db)):
    return crud_invoice.create_invoice(db, invoice)

@router.get("/invoice/{invoice_id}", response_model=schema_invoice.Invoice, tags=tags)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = crud_invoice.get_invoice(db, invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice

@router.get("/invoices", response_model=schema_invoice.Invoices, tags=tags)
def read_invoices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    invoices = crud_invoice.get_invoices(db, skip=skip, limit=limit)
    total_count = db.query(model_invoice.Invoice).count()
    return {
        "invoices": invoices,
        "total_count": total_count
    }

@router.put("/invoices", response_model=schema_invoice.Invoice, tags=tags)
def update_invoice(invoice: schema_invoice.InvoiceUpdate, db: Session = Depends(get_db)):
    db_invoice = crud_invoice.get_invoice(db, invoice.id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    db_invoice = crud_invoice.update_invoice(db, invoice)
    return db_invoice

@router.delete("/invoice/{invoice_id}", tags=tags)
def delete_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = crud_invoice.get_invoice(db, invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return crud_invoice.delete_invoice(db, invoice_id)
