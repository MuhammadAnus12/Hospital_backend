from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import treatment as model_treatment
from cruds import treatment as crud_treatment
from schemas import treatment as schema_treatment


router = APIRouter()
tags = ["Treatment"]

@router.post("/treatment", response_model=schema_treatment.Treatment, tags=tags)
def create_treatment(treatment: schema_treatment.TreatmentCreate, db: Session = Depends(get_db)):
    return crud_treatment.create_treatment(db, treatment)

@router.get("/treatment/{treatment_id}", response_model=schema_treatment.Treatment, tags=tags)
def read_treatment(treatment_id: int, db: Session = Depends(get_db)):
    db_treatment = crud_treatment.get_treatment(db, treatment_id)
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    return db_treatment

@router.get("/treatments", response_model=schema_treatment.Treatments, tags=tags)
def read_treatments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    treatments = crud_treatment.get_treatments(db, skip=skip, limit=limit)
    total_count = db.query(model_treatment.Treatment).count()
    return {
        "treatments": treatments,
        "total_count": total_count
    }

@router.put("/treatments", response_model=schema_treatment.Treatment, tags=tags)
def update_treatment(treatment: schema_treatment.TreatmentUpdate, db: Session = Depends(get_db)):

    db_treatment = crud_treatment.get_treatment(db, treatment.id)
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    db_treatment = crud_treatment.update_treatment(db, treatment)
    return db_treatment

@router.delete("/treatment/{treatment_id}", tags=tags)
def delete_treatment(treatment_id: int, db: Session = Depends(get_db)):
    db_treatment = crud_treatment.get_treatment(db, treatment_id)
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    return crud_treatment.delete_treatment(db, treatment_id)

@router.post("/treatment/search", response_model=schema_treatment.Treatment, tags=tags)
def search_treatment(treatment: schema_treatment.SearchTreatment, db: Session = Depends(get_db)):
    db_treatment = crud_treatment.search_treatment(db, treatment)
    if db_treatment is None:
        raise HTTPException(status_code=404, detail="Treatment not found")
    return db_treatment

