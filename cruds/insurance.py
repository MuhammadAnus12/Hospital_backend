from sqlalchemy.orm import Session
from models import insurance as model_insurance,patient as model_patient
from schemas import insurance as schema_insurance
from typing import List


def create_insurance(db: Session, insurance: schema_insurance.InsuranceCreate):
    db_insurance = model_insurance.Insurance(**insurance.dict())
    db.add(db_insurance)
    db.commit()
    db.refresh(db_insurance)
    return db_insurance

def get_insurances(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_insurance.Insurance).offset(skip).limit(limit).all()

def get_insurance(db: Session, insurance_id: int):
    db_insurance = db.query(model_insurance.Insurance).filter(
        model_insurance.Insurance.id == insurance_id).first()
    if db_insurance is None:
        return None
    return db_insurance

def update_insurance(db: Session, insurance: schema_insurance.InsuranceUpdate):
    db_insurance = db.query(model_insurance.Insurance).filter(
        model_insurance.Insurance.id == insurance.id).first()
    if db_insurance is None:
        return None
    for key, value in insurance.model_dump().items():
        setattr(db_insurance, key, value)
    db.commit()
    db.refresh(db_insurance)
    return db_insurance

def delete_insurance(db: Session, insurance_id: int):
    db_insurance = db.query(model_insurance.Insurance).filter(
        model_insurance.Insurance.id == insurance_id).first()
    if db_insurance is None:
        return None
    db.delete(db_insurance)
    db.commit()
    return db_insurance

def check_insurance_child(db:Session,insurance_id:int)->bool:
    if db.query(model_patient.Patient).filter(model_patient.Patient.insurance_id==insurance_id):
        return True
    return False

