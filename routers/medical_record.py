from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import medical_record as model_medical_record
from cruds import medical_record as crud_medical_record
from schemas import medical_record as schema_medical_record


router = APIRouter()
tags = ["Medical Record"]

@router.post("/medical_record", response_model=schema_medical_record.MedicalRecord, tags=tags)
def create_medical_record(medical_record: schema_medical_record.MedicalRecordCreate, db: Session = Depends(get_db)):
    return crud_medical_record.create_medical_record(db, medical_record)

@router.get("/medical_record/{medical_record_id}", response_model=schema_medical_record.MedicalRecord, tags=tags)
def read_medical_record(medical_record_id: int, db: Session = Depends(get_db)):
    db_medical_record = crud_medical_record.get_medical_record(db, medical_record_id)
    if db_medical_record is None:
        raise HTTPException(status_code=404, detail="Medical Record not found")
    return db_medical_record

@router.get("/medical_records", response_model=schema_medical_record.MedicalRecords, tags=tags)
def read_medical_records(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medical_records = crud_medical_record.get_medical_records(db, skip=skip, limit=limit)
    total_count = db.query(model_medical_record.MedicalRecord).count()
    return {
        "medical_records": medical_records,
        "total_count": total_count
    }

@router.put("/medical_record", response_model=schema_medical_record.MedicalRecord, tags=tags)
def update_medical_record(medical_record: schema_medical_record.MedicalRecordUpdate, db: Session = Depends(get_db)):
    db_medical_record = crud_medical_record.get_medical_record(db, medical_record.id)
    if db_medical_record is None:
        raise HTTPException(status_code=404, detail="Medical Record not found")
    db_medical_record = crud_medical_record.update_medical_record(db, medical_record)
    return db_medical_record

@router.delete("/medical_record/{medical_record_id}", tags=tags)
def delete_medical_record(medical_record_id: int, db: Session = Depends(get_db)):
    db_medical_record = crud_medical_record.get_medical_record(db, medical_record_id)
    if db_medical_record is None:
        raise HTTPException(status_code=404, detail="Medical Record not found")
    db_medical_child=crud_medical_record.check_medical_child(db,medical_record_id)
    if db_medical_child is True:
        raise HTTPException(status_code=404,detail="Medical Child Exist")
    return crud_medical_record.delete_medical_record(db, medical_record_id)
