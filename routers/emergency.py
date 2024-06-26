from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import emergency as model_emergency
from cruds import emergency as crud_emergency
from schemas import emergency as schema_emergency


router = APIRouter()
tags = ["Emergency"]

@router.post("/emergency", response_model=schema_emergency.Emergency, tags=tags)
def create_emergency(emergency: schema_emergency.EmergencyCreate, db: Session = Depends(get_db)):
    return crud_emergency.create_emergency(db, emergency)

@router.get("/emergency/{emergency_id}", response_model=schema_emergency.Emergency, tags=tags)
def read_emergency(emergency_id: int, db: Session = Depends(get_db)):
    db_emergency = crud_emergency.get_emergency(db, emergency_id)
    if db_emergency is None:
        raise HTTPException(status_code=404, detail="Emergency not found")
    return db_emergency

@router.get("/emergencies", response_model=schema_emergency.Emergencies, tags=tags)
def read_emergencies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    emergencies = crud_emergency.get_emergencies(db, skip=skip, limit=limit)
    total_count = db.query(model_emergency.Emergency).count()
    return {
        "emergencies": emergencies,
        "total_count": total_count
    }

@router.put("/emergency", response_model=schema_emergency.Emergency, tags=tags)
def update_emergency(emergency: schema_emergency.EmergencyUpdate, db: Session = Depends(get_db)):
    db_emergency = crud_emergency.get_emergency(db, emergency.id)
    if db_emergency is None:
        raise HTTPException(status_code=404, detail="Emergency not found")
    db_emergency = crud_emergency.update_emergency(db, emergency)
    return db_emergency

@router.delete("/emergency/{emergency_id}", tags=tags)
def delete_emergency(emergency_id: int, db: Session = Depends(get_db)):
    db_emergency = crud_emergency.get_emergency(db, emergency_id)
    if db_emergency is None:
        raise HTTPException(status_code=404, detail="Emergency not found")
    return crud_emergency.delete_emergency(db, emergency_id)

