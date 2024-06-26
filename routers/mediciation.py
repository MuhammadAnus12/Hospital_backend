from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import mediciaton as model_medication
from cruds import mediciation as crud_medication
from schemas import mediciation as schema_medication


router = APIRouter()
tags = ["Medication"]

@router.post("/medication", response_model=schema_medication.Medication, tags=tags)
def create_medication(medication: schema_medication.MedicationCreate, db: Session = Depends(get_db)):
    return crud_medication.create_medication(db, medication)

@router.get("/medication/{medication_id}", response_model=schema_medication.Medication, tags=tags)
def read_medication(medication_id: int, db: Session = Depends(get_db)):
    db_medication = crud_medication.get_medication(db, medication_id)
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    return db_medication

@router.get("/medications", response_model=schema_medication.Medications, tags=tags)
def read_medications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medications = crud_medication.get_medications(db, skip=skip, limit=limit)
    total_count = db.query(model_medication.Mediciation).count()
    return {
        "medications": medications,
        "total_count": total_count
    }

@router.put("/medications", response_model=schema_medication.Medication, tags=tags)
def update_medication(medication: schema_medication.MedicationUpdate, db: Session = Depends(get_db)):
    db_medication = crud_medication.get_medication(db, medication.id)
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    db_medication = crud_medication.update_medication(db, medication)
    return db_medication

@router.delete("/medication/{medication_id}", tags=tags)
def delete_medication(medication_id: int, db: Session = Depends(get_db)):
    db_medication = crud_medication.get_medication(db, medication_id)
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    return crud_medication.delete_medication(db, medication_id)

