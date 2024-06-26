from sqlalchemy.orm import Session
from models import mediciaton as model_medication
from schemas import mediciation as schema_medication
from typing import List

def create_medication(db: Session, medication: schema_medication.MedicationCreate):
    db_medication = model_medication.Mediciation(**medication.model_dump())
    db.add(db_medication)
    db.commit()
    db.refresh(db_medication)
    return db_medication

def get_medications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_medication.Mediciation).offset(skip).limit(limit).all()

def get_medication(db: Session, medication_id: int):
    db_medication = db.query(model_medication.Mediciation).filter(
        model_medication.Mediciation.id == medication_id).first()
    if db_medication is None:
        return None
    return db_medication

def update_medication(db: Session, medication: schema_medication.MedicationUpdate):
    db_medication = db.query(model_medication.Mediciation).filter(
        model_medication.Mediciation.id == medication.id).first()
    if db_medication is None:
        return None
    for key, value in medication.model_dump().items():
        setattr(db_medication, key, value)
    db.commit()
    db.refresh(db_medication)
    return db_medication

def delete_medication(db: Session, medication_id: int):
    db_medication = db.query(model_medication.Mediciation).filter(
        model_medication.Mediciation.id == medication_id).first()
    if db_medication is None:
        return None
    db.delete(db_medication)
    db.commit()
    return db_medication

