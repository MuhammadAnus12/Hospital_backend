from sqlalchemy.orm import Session
from models import payment as model_payment
from schemas import payment as schema_payment
from typing import List

def create_payment(db: Session, payment: schema_payment.PaymentCreate):
    db_payment = model_payment.Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def get_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_payment.Payment).offset(skip).limit(limit).all()

def get_payment(db: Session, payment_id: int):
    db_payment = db.query(model_payment.Payment).filter(
        model_payment.Payment.id == payment_id).first()
    if db_payment is None:
        return None
    return db_payment

def update_payment(db: Session, payment: schema_payment.PaymentUpdate):
    db_payment = db.query(model_payment.Payment).filter(
        model_payment.Payment.id == payment.id).first()
    if db_payment is None:
        return None
    for key, value in payment.model_dump().items():
        setattr(db_payment, key, value)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def delete_payment(db: Session, payment_id: int):
    db_payment = db.query(model_payment.Payment).filter(
        model_payment.Payment.id == payment_id).first()
    if db_payment is None:
        return None
    db.delete(db_payment)
    db.commit()
    return db_payment

