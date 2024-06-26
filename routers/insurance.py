from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import insurance as model_insurance
from cruds import insurance as crud_insurance
from schemas import insurance as schema_insurance


router = APIRouter()
tags = ["Insurance"]

@router.post("/insurance", response_model=schema_insurance.Insurance, tags=tags)
def create_insurance(insurance: schema_insurance.InsuranceCreate, db: Session = Depends(get_db)):
    return crud_insurance.create_insurance(db, insurance)

@router.get("/insurance/{insurance_id}", response_model=schema_insurance.Insurance, tags=tags)
def read_insurance(insurance_id: int, db: Session = Depends(get_db)):
    db_insurance = crud_insurance.get_insurance(db, insurance_id)
    if db_insurance is None:
        raise HTTPException(status_code=404, detail="Insurance not found")
    return db_insurance

@router.get("/insurances", response_model=schema_insurance.Insurances, tags=tags)
def read_insurances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    insurances = crud_insurance.get_insurances(db, skip=skip, limit=limit)
    total_count = db.query(model_insurance.Insurance).count()
    return {
        "insurances": insurances,
        "total_count": total_count
    }

@router.put("/insurance", response_model=schema_insurance.Insurance, tags=tags)
def update_insurance(insurance: schema_insurance.InsuranceUpdate, db: Session = Depends(get_db)):

    db_insurance = crud_insurance.get_insurance(db, insurance.id)
    if db_insurance is None:
        raise HTTPException(status_code=404, detail="Insurance not found")
    db_insurance = crud_insurance.update_insurance(db, insurance)
    return db_insurance

@router.delete("/insurance/{insurance_id}", tags=tags)
def delete_insurance(insurance_id: int, db: Session = Depends(get_db)):
    db_insurance = crud_insurance.get_insurance(db, insurance_id)
    if db_insurance is None:
        raise HTTPException(status_code=404, detail="Insurance not found")
    return crud_insurance.delete_insurance(db, insurance_id)
