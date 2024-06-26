from sqlalchemy.orm import Session
from models import doctor as model_doctor
from schemas import doctor as schema_doctor
from typing import List

def create_doctor(db: Session, doctor: schema_doctor.DoctorCreate):
    db_doctor=model_doctor.Doctor(**doctor.model_dump())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def get_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(model_doctor.Doctor).filter(model_doctor.Doctor.id == doctor_id).first()
    if db_doctor is None:
        return None
    return db_doctor

def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_doctor.Doctor).offset(skip).limit(limit).all()

def update_doctor(db: Session, doctor: schema_doctor.DoctorUpdate):
    db_doctor = db.query(model_doctor.Doctor).filter(model_doctor.Doctor.id == doctor.id).first()
    if db_doctor is None:
        return None
    for key, value in doctor.model_dump().items():
        setattr(db_doctor, key, value)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def delete_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(model_doctor.Doctor).filter(model_doctor.Doctor.id == doctor_id).first()
    if db_doctor is None:
        return None
    db.delete(db_doctor)
    db.commit()
    return db_doctor

def search_doctor(db: Session, doctor: schema_doctor.SearchDoctor):
    db_doctor = db.query(model_doctor.Doctor).filter(model_doctor.Doctor.first_name == doctor.first_name).filter(model_doctor.Doctor.last_name == doctor.last_name).filter(model_doctor.Doctor.specialty == doctor.specialty).first()
    if db_doctor is None:
        return None
    return db_doctor