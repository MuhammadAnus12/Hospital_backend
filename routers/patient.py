from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import patient as model_patient
from cruds import patient as crud_patient
from schemas import patient as schema_patient


router = APIRouter()
tags = ["Patient"]

@router.post("/patient", response_model=schema_patient.Patient, tags=tags)
def create_patient(patient: schema_patient.PatientCreate, db: Session = Depends(get_db)):
    return crud_patient.create_patient(db, patient)

@router.get("/patient/{patient_id}", response_model=schema_patient.Patient, tags=tags)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud_patient.get_patient(db, patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient

@router.get("/patients", response_model=schema_patient.Patients, tags=tags)
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = crud_patient.get_patients(db, skip=skip, limit=limit)
    total_count = db.query(model_patient.Patient).count()
    return {
        "patients": patients,
        "total_count": total_count
    }

@router.put("/patients", response_model=schema_patient.Patient, tags=tags)
def update_patient(patient: schema_patient.PatientUpdate, db: Session = Depends(get_db)):
    db_patient = crud_patient.get_patient(db, patient.id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    db_patient = crud_patient.update_patient(db, patient)
    return db_patient

@router.delete("/patient/{patient_id}", tags=tags)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    db_patient = crud_patient.get_patient(db, patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return crud_patient.delete_patient(db, patient_id)

@router.post("/patient/search", response_model=schema_patient.Patient, tags=tags)
def search_patient(patient: schema_patient.SearchPatient, db: Session = Depends(get_db)):
    db_patient = crud_patient.search_patient(db, patient)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_patient