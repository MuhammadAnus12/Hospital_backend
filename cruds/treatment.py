from sqlalchemy.orm import Session
from models import treatment as model_treatment
from schemas import treatment as schema_treatment
from typing import List


def create_treatment(db: Session, treatment: schema_treatment.TreatmentCreate):
    db_treatment = model_treatment.Treatment(**treatment.model_dump())
    db.add(db_treatment)
    db.commit()
    db.refresh(db_treatment)
    return db_treatment

def get_treatments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_treatment.Treatment).offset(skip).limit(limit).all()

def get_treatment(db: Session, treatment_id: int):
    db_treatment = db.query(model_treatment.Treatment).filter(
        model_treatment.Treatment.id == treatment_id).first()
    if db_treatment is None:
        return None
    return db_treatment

def update_treatment(db: Session, treatment: schema_treatment.TreatmentUpdate):
    db_treatment = db.query(model_treatment.Treatment).filter(
        model_treatment.Treatment.id == treatment.id).first()
    if db_treatment is None:
        return None
    for key, value in treatment.model_dump().items():
        setattr(db_treatment, key, value)
    db.commit()
    db.refresh(db_treatment)
    return db_treatment

def delete_treatment(db: Session, treatment_id: int):
    db_treatment = db.query(model_treatment.Treatment).filter(
        model_treatment.Treatment.id == treatment_id).first()
    if db_treatment is None:
        return None
    db.delete(db_treatment)
    db.commit()
    return db_treatment

def search_treatment(db: Session, treatment: schema_treatment.SearchTreatment):
    db_treatment = db.query(model_treatment.Treatment).filter
    (model_treatment.Treatment.diagnosis == treatment.diagnosis).filter
    (model_treatment.Treatment.treatment_plan == treatment.treatment_plan).first()
    if db_treatment is None:
        return None
    return db_treatment