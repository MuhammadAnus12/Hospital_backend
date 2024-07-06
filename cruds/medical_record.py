from sqlalchemy.orm import Session
from models import medical_record as model_medical_record,patient as model_patient
from schemas import medical_record as schema_medical_record
from typing import List


def create_medical_record(db: Session, medical_record: schema_medical_record.MedicalRecordCreate):
    db_medical_record = model_medical_record.MedicalRecord(**medical_record.dict())
    db.add(db_medical_record)
    db.commit()
    db.refresh(db_medical_record)
    return db_medical_record

def get_medical_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_medical_record.MedicalRecord).offset(skip).limit(limit).all()

def get_medical_record(db: Session, medical_record_id: int):
    db_medical_record = db.query(model_medical_record.MedicalRecord).filter(
        model_medical_record.MedicalRecord.id == medical_record_id).first()
    if db_medical_record is None:
        return None
    return db_medical_record

def update_medical_record(db: Session, medical_record: schema_medical_record.MedicalRecordUpdate):
    db_medical_record = db.query(model_medical_record.MedicalRecord).filter(
        model_medical_record.MedicalRecord.id == medical_record.id).first()
    if db_medical_record is None:
        return None
    for key, value in medical_record.model_dump().items():
        setattr(db_medical_record, key, value)
    db.commit()
    db.refresh(db_medical_record)
    return db_medical_record

def delete_medical_record(db: Session, medical_record_id: int):
    db_medical_record = db.query(model_medical_record.MedicalRecord).filter(
        model_medical_record.MedicalRecord.id == medical_record_id).first()
    if db_medical_record is None:
        return None
    db.delete(db_medical_record)
    db.commit()
    return db_medical_record

def check_medical_child(db:Session,medical_record_id:int)->bool:
    if db.query(model_patient.Patient).filter(model_patient.Patient.medical_record_id==medical_record_id).first():
        return True
    return False
