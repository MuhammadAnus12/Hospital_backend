from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import labtest as model_labtest
from cruds import labtest as crud_labtest
from schemas import labtest as schema_labtest


router = APIRouter()
tags = ["LabTest"]


@router.post("/labtest", response_model=schema_labtest.LabTest, tags=tags)
def create_labtest(labtest: schema_labtest.LabTestCreate, db: Session = Depends(get_db)):
    db_patient = crud_labtest.check_patient(db, labtest.patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    db_labtechnician = crud_labtest.check_lab_technician(
        db, labtest.lab_technician_id)
    if db_labtechnician is None:
        raise HTTPException(status_code=404, detail="Lab Technician not found")
    return crud_labtest.create_labtest(db, labtest)


@router.get("/labtest/{labtest_id}", response_model=schema_labtest.LabTest, tags=tags)
def read_labtest(labtest_id: int, db: Session = Depends(get_db)):
    db_labtest = crud_labtest.get_labtest(db, labtest_id)
    if db_labtest is None:
        raise HTTPException(status_code=404, detail="LabTest not found")
    return db_labtest


@router.get("/labtests", response_model=schema_labtest.LabTests, tags=tags)
def read_labtests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    labtests = crud_labtest.get_labtests(db, skip=skip, limit=limit)
    total_count = db.query(model_labtest.LabTest).count()
    return {
        "labtests": labtests,
        "total_count": total_count
    }


@router.put("/labtests", response_model=schema_labtest.LabTest, tags=tags)
def update_labtest(labtest: schema_labtest.LabTestUpdate, db: Session = Depends(get_db)):
    db_labtest = crud_labtest.get_labtest(db, labtest.id)
    if db_labtest is None:
        raise HTTPException(status_code=404, detail="LabTest not found")
    db_patient = crud_labtest.check_patient(db, labtest.patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    db_labtechnician = crud_labtest.check_lab_technician(
        db, labtest.lab_technician_id)
    if db_labtechnician is None:
        raise HTTPException(status_code=404, detail="Lab Technician not found")
    db_labtest = crud_labtest.update_labtest(db, labtest)
    return db_labtest


@router.delete("/labtest/{labtest_id}", tags=tags)
def delete_labtest(labtest_id: int, db: Session = Depends(get_db)):
    db_labtest = crud_labtest.get_labtest(db, labtest_id)
    if db_labtest is None:
        raise HTTPException(status_code=404, detail="LabTest not found")
    return crud_labtest.delete_labtest(db, labtest_id)
