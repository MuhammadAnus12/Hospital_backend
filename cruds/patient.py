from sqlalchemy.orm import Session
from models import (patient as model_patient,
emergency as model_emergency,
medical_record as model_medical_record,
insurance as model_insurance,
appointment as model_appointment,
treatment as model_treatment,
labtest as model_labtest,
invoice as model_invoice,
)
from schemas import patient as schema_patient
from typing import List

def create_patient(db: Session, patient: schema_patient.PatientCreate):
    db_patient=model_patient.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def check_emergency(db:Session,emergency_id:int):
    db_emergency=db.query(model_emergency.Emergency).filter(model_emergency.Emergency.id==emergency_id).first()
    if db_emergency is None:
        return None
    return db_emergency

def check_insurance(db:Session,insurance_id:int):
    db_insurance=db.query(model_insurance.Insurance).filter(model_insurance.Insurance.id==insurance_id).first()
    if db_insurance is None:
        return None
    return db_insurance

def check_medical_record(db:Session,medical_record_id:int):
    db_medical_record=db.query(model_medical_record.MedicalRecord).filter(model_medical_record.MedicalRecord.id==medical_record_id).first()
    if db_medical_record is None:
        return None
    return db_medical_record

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

def check_patient_in_child(db: Session, patient_id: int) -> bool:
    if db.query(model_appointment.Appointment).filter(model_appointment.Appointment.patient_id == patient_id).first():
        return True
    if db.query(model_treatment.Treatment).filter(model_treatment.Treatment.patient_id == patient_id).first():
        return True
    if db.query(model_labtest.LabTest).filter(model_labtest.LabTest.patient_id == patient_id).first():
        return True
    if db.query(model_invoice.Invoice).filter(model_invoice.Invoice.patient_id == patient_id).first():
        return True
    return False