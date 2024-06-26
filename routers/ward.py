from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import ward as model_ward
from cruds import ward as crud_ward
from schemas import ward as schema_ward


router = APIRouter()
tags = ["Ward"]

@router.post("/ward", response_model=schema_ward.Ward, tags=tags)
def create_ward(ward: schema_ward.WardCreate, db: Session = Depends(get_db)):
    return crud_ward.create_ward(db, ward)

@router.get("/ward/{ward_id}", response_model=schema_ward.Ward, tags=tags)
def read_ward(ward_id: int, db: Session = Depends(get_db)):
    db_ward = crud_ward.get_ward(db, ward_id)
    if db_ward is None:
        raise HTTPException(status_code=404, detail="Ward not found")
    return db_ward

@router.get("/wards", response_model=schema_ward.Wards, tags=tags)
def read_wards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    wards = crud_ward.get_wards(db, skip=skip, limit=limit)
    total_count = db.query(model_ward.Ward).count()
    return {
        "wards": wards,
        "total_count": total_count
    }

@router.put("/ward", response_model=schema_ward.Ward, tags=tags)
def update_ward(ward: schema_ward.WardUpdate, db: Session = Depends(get_db)):
    db_ward = crud_ward.get_ward(db, ward.id)
    if db_ward is None:
        raise HTTPException(status_code=404, detail="Ward not found")
    db_ward = crud_ward.update_ward(db, ward)
    return db_ward

@router.delete("/ward/{ward_id}", tags=tags)
def delete_ward(ward_id: int, db: Session = Depends(get_db)):
    db_ward = crud_ward.get_ward(db, ward_id)
    if db_ward is None:
        raise HTTPException(status_code=404, detail="Ward not found")
    return crud_ward.delete_ward(db, ward_id)

