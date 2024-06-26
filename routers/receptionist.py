from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import receptionist as model_receptionist
from cruds import receptionist as crud_receptionist
from schemas import receptionist as schema_receptionist


router = APIRouter()
tags = ["Receptionist"]


@router.post("/receptionist", response_model=schema_receptionist.Receptionist, tags=tags)
def create_receptionist(receptionist: schema_receptionist.ReceptionistCreate, db: Session = Depends(get_db)):
    return crud_receptionist.create_receptionist(db, receptionist)


@router.get("/receptionist/{receptionist_id}", response_model=schema_receptionist.Receptionist, tags=tags)
def read_receptionist(receptionist_id: int, db: Session = Depends(get_db)):
    db_receptionist = crud_receptionist.get_receptionist(db, receptionist_id)
    if db_receptionist is None:
        raise HTTPException(status_code=404, detail="Receptionist not found")
    return db_receptionist


@router.get("/receptionists", response_model=schema_receptionist.Receptionists, tags=tags)
def read_receptionists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    receptionists = crud_receptionist.get_receptionists(
        db, skip=skip, limit=limit)
    total_count = db.query(model_receptionist.Receptionist).count()
    return {
        "receptionists": receptionists,
        "total_count": total_count
    }


@router.put("/receptionists", response_model=schema_receptionist.Receptionist, tags=tags)
def update_receptionist(receptionist: schema_receptionist.ReceptionistUpdate, db: Session = Depends(get_db)):
    db_receptionist = crud_receptionist.get_receptionist(db, receptionist.id)
    if db_receptionist is None:
        raise HTTPException(status_code=404, detail="Receptionist not found")
    db_receptionist = crud_receptionist.update_receptionist(db, receptionist)
    return db_receptionist


@router.delete("/receptionist/{receptionist_id}", tags=tags)
def delete_receptionist(receptionist_id: int, db: Session = Depends(get_db)):
    db_receptionist = crud_receptionist.get_receptionist(db, receptionist_id)
    if db_receptionist is None:
        raise HTTPException(status_code=404, detail="Receptionist not found")
    return crud_receptionist.delete_receptionist(db, receptionist_id)


@router.post("/receptionist/search", response_model=schema_receptionist.Receptionist, tags=tags)
def search_receptionist(receptionist: schema_receptionist.SearchReceptionist, db: Session = Depends(get_db)):
    db_receptionist = crud_receptionist.search_receptionist(db, receptionist)
    if db_receptionist is None:
        raise HTTPException(status_code=404, detail="Receptionist not found")
    return db_receptionist
