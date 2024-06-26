from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import labtechnician as model_labtechnician
from cruds import labtechnician as crud_labtechnician
from schemas import labtechnician as schema_labtechnician


router = APIRouter()
tags = ["LabTechnician"]

@router.post("/labtechnician", response_model=schema_labtechnician.LabTechnician, tags=tags)
def create_labtechnician(labtechnician: schema_labtechnician.LabTechnicianCreate, db: Session = Depends(get_db)):
    return crud_labtechnician.create_labtechnician(db, labtechnician)

@router.get("/labtechnician/{labtechnician_id}", response_model=schema_labtechnician.LabTechnician, tags=tags)
def read_labtechnician(labtechnician_id: int, db: Session = Depends(get_db)):
    db_labtechnician = crud_labtechnician.get_labtechnician(db, labtechnician_id)
    if db_labtechnician is None:
        raise HTTPException(status_code=404, detail="LabTechnician not found")
    return db_labtechnician

@router.get("/labtechnicians", response_model=schema_labtechnician.LabTechnicians, tags=tags)
def read_labtechnicians(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    labtechnicians = crud_labtechnician.get_labtechnicians(db, skip=skip, limit=limit)
    total_count = db.query(model_labtechnician.LabTechnician).count()
    return {
        "labtechnicians": labtechnicians,
        "total_count": total_count
    }

@router.put("/labtechnicians", response_model=schema_labtechnician.LabTechnician, tags=tags)
def update_labtechnician(labtechnician: schema_labtechnician.LabTechnicianUpdate, db: Session = Depends(get_db)):

    db_labtechnician = crud_labtechnician.get_labtechnician(db, labtechnician.id)
    if db_labtechnician is None:
        raise HTTPException(status_code=404, detail="LabTechnician not found")
    db_labtechnician = crud_labtechnician.update_labtechnician(db, labtechnician)
    return db_labtechnician

@router.delete("/labtechnician/{labtechnician_id}", tags=tags)
def delete_labtechnician(labtechnician_id: int, db: Session = Depends(get_db)):
    db_labtechnician = crud_labtechnician.get_labtechnician(db, labtechnician_id)
    if db_labtechnician is None:
        raise HTTPException(status_code=404, detail="LabTechnician not found")
    return crud_labtechnician.delete_labtechnician(db, labtechnician_id)
