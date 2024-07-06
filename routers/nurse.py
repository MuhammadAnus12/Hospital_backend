from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import nurse as model_nurse
from cruds import nurse as crud_nurse
from schemas import nurse as schema_nurse


router = APIRouter()
tags = ["Nurse"]

@router.post("/nurse", response_model=schema_nurse.Nurse, tags=tags)
def create_nurse(nurse: schema_nurse.NurseCreate, db: Session = Depends(get_db)):
    db_department=crud_nurse.check_department(db,nurse.department_id)
    if db_department is None:
        raise HTTPException(status_code=404,detail="Department not found")
    return crud_nurse.create_nurse(db, nurse)

@router.get("/nurse/{nurse_id}", response_model=schema_nurse.Nurse, tags=tags)
def read_nurse(nurse_id: int, db: Session = Depends(get_db)):
    db_nurse = crud_nurse.get_nurse(db, nurse_id)
    if db_nurse is None:
        raise HTTPException(status_code=404, detail="Nurse not found")
    return db_nurse

@router.get("/nurses", response_model=schema_nurse.Nurses, tags=tags)
def read_nurses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    nurses = crud_nurse.get_nurses(db, skip=skip, limit=limit)
    total_count = db.query(model_nurse.Nurse).count()
    return {
        "nurses": nurses,
        "total_count": total_count
    }

@router.put("/nurses", response_model=schema_nurse.Nurse, tags=tags)
def update_nurse(nurse: schema_nurse.NurseUpdate, db: Session = Depends(get_db)):
    db_nurse = crud_nurse.get_nurse(db, nurse.id)
    if db_nurse is None:
        raise HTTPException(status_code=404, detail="Nurse not found")
    db_department=crud_nurse.check_department(db,nurse.department_id)
    if db_department is None:
        raise HTTPException(status_code=404,detail="Department not found")
    db_nurse = crud_nurse.update_nurse(db, nurse)
    return db_nurse

@router.delete("/nurse/{nurse_id}", tags=tags)
def delete_nurse(nurse_id: int, db: Session = Depends(get_db)):
    db_nurse = crud_nurse.get_nurse(db, nurse_id)
    if db_nurse is None:
        raise HTTPException(status_code=404, detail="Nurse not found")
    return crud_nurse.delete_nurse(db, nurse_id)

@router.post("/nurse/search", response_model=schema_nurse.Nurse, tags=tags)
def search_nurse(nurse: schema_nurse.SearchNurse, db: Session = Depends(get_db)):
    db_nurse = crud_nurse.search_nurse(db, nurse)
    if db_nurse is None:
        raise HTTPException(status_code=404, detail="Nurse not found")
    return db_nurse