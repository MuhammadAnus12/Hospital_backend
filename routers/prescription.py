from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import prescription as model_prescription
from cruds import prescription as crud_prescription
from schemas import prescription as schema_prescription


router = APIRouter()
tags = ["Prescription"]


@router.post("/prescription", response_model=schema_prescription.Prescription, tags=tags)
def create_prescription(prescription: schema_prescription.PrescriptionCreate, db: Session = Depends(get_db)):
    return crud_prescription.create_prescription(db, prescription)


@router.get("/prescription/{prescription_id}", response_model=schema_prescription.Prescription, tags=tags)
def read_prescription(prescription_id: int, db: Session = Depends(get_db)):
    db_prescription = crud_prescription.get_prescription(db, prescription_id)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return db_prescription


@router.get("/prescriptions", response_model=schema_prescription.Prescriptions, tags=tags)
def read_prescriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prescriptions = crud_prescription.get_prescriptions(
        db, skip=skip, limit=limit)
    total_count = db.query(model_prescription.Prescription).count()
    return {
        "prescriptions": prescriptions,
        "total_count": total_count
    }


@router.put("/prescriptions", response_model=schema_prescription.Prescription, tags=tags)
def update_prescription(prescription: schema_prescription.PrescriptionUpdate, db: Session = Depends(get_db)):

    db_prescription = crud_prescription.get_prescription(db, prescription.id)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    db_prescription = crud_prescription.update_prescription(db, prescription)
    return db_prescription


@router.delete("/prescription/{prescription_id}", tags=tags)
def delete_prescription(prescription_id: int, db: Session = Depends(get_db)):
    db_prescription = crud_prescription.get_prescription(db, prescription_id)
    if db_prescription is None:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return crud_prescription.delete_prescription(db, prescription_id)
