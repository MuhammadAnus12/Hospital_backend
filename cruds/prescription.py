from sqlalchemy.orm import Session
from models import prescription as model_prescription
from schemas import prescription as schema_prescription
from typing import List

def create_prescription(db: Session, prescription: schema_prescription.PrescriptionCreate):
    db_prescription = model_prescription.Prescription(**prescription.model_dump())
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription


def get_prescriptions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_prescription.Prescription).offset(skip).limit(limit).all()

def get_prescription(db: Session, prescription_id: int):
    db_prescription = db.query(model_prescription.Prescription).filter(
        model_prescription.Prescription.id == prescription_id).first()
    if db_prescription is None:
        return None
    return db_prescription

def update_prescription(db: Session, prescription: schema_prescription.PrescriptionUpdate):
    db_prescription = db.query(model_prescription.Prescription).filter(
        model_prescription.Prescription.id == prescription.id).first()
    if db_prescription is None:
        return None
    for key, value in prescription.model_dump().items():
        setattr(db_prescription, key, value)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription

def delete_prescription(db: Session, prescription_id: int):
    db_prescription = db.query(model_prescription.Prescription).filter(
        model_prescription.Prescription.id == prescription_id).first()
    if db_prescription is None:
        return None
    db.delete(db_prescription)
    db.commit()
    return db_prescription

