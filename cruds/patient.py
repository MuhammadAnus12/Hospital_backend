from sqlalchemy.orm import Session
from models import patient as model_patient
from schemas import patient as schema_patient
from typing import List

def create_patient(db: Session, patient: schema_patient.PatientCreate):
    db_patient=model_patient.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient(db: Session, patient_id: int):
    db_patient = db.query(model_patient.Patient).filter(model_patient.Patient.id == patient_id).first()
    if db_patient is None:
        return None
    return db_patient

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_patient.Patient).offset(skip).limit(limit).all()

def update_patient(db: Session, patient: schema_patient.PatientUpdate):
    db_patient = db.query(model_patient.Patient).filter(model_patient.Patient.id == patient.id).first()
    if db_patient is None:
        return None
    for key, value in patient.model_dump().items():
        setattr(db_patient, key, value)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(model_patient.Patient).filter(model_patient.Patient.id == patient_id).first()
    if db_patient is None:
        return None
    db.delete(db_patient)
    db.commit()
    return db_patient

def search_patient(db: Session, patient: schema_patient.SearchPatient):
    db_patient = db.query(model_patient.Patient).filter(model_patient.Patient.first_name == patient.first_name).filter(model_patient.Patient.last_name == patient.last_name).filter(model_patient.Patient.date_of_birth == patient.date_of_birth).first()
    if db_patient is None:
        return None
    return db_patient