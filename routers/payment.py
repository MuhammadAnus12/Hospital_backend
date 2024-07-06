from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import payment as model_payment
from cruds import payment as crud_payment
from schemas import payment as schema_payment

router = APIRouter()
tags = ["Payment"]

@router.post("/payment", response_model=schema_payment.Payment, tags=tags)
def create_payment(payment: schema_payment.PaymentCreate, db: Session = Depends(get_db)):
    db_invoice=crud_payment.check_invoice(db,payment.invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404,detail="Invoice Not found")
    return crud_payment.create_payment(db, payment)

@router.get("/payment/{payment_id}", response_model=schema_payment.Payment, tags=tags)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = crud_payment.get_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment

@router.get("/payments", response_model=schema_payment.Payments, tags=tags)
def read_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    payments = crud_payment.get_payments(db, skip=skip, limit=limit)
    total_count = db.query(model_payment.Payment).count()
    return {
        "payments": payments,
        "total_count": total_count
    }

@router.put("/payment", response_model=schema_payment.Payment, tags=tags)
def update_payment(payment: schema_payment.PaymentUpdate, db: Session = Depends(get_db)):

    db_payment = crud_payment.get_payment(db, payment.id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    db_invoice=crud_payment.check_invoice(db,payment.invoice_id)
    if db_invoice is None:
        raise HTTPException(status_code=404,detail="Invoice Not found")
    db_payment = crud_payment.update_payment(db, payment)
    return db_payment

@router.delete("/payment/{payment_id}", tags=tags)
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    db_payment = crud_payment.get_payment(db, payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return crud_payment.delete_payment(db, payment_id)
