from sqlalchemy.orm import Session
from models import labtest as model_labtest,patient as model_patient,labtechnician as model_labtechnician
from schemas import labtest as schema_labtest
from typing import List


def create_labtest(db: Session, labtest: schema_labtest.LabTestCreate):
    db_labtest = model_labtest.LabTest(**labtest.model_dump())
    db.add(db_labtest)
    db.commit()
    db.refresh(db_labtest)
    return db_labtest

def check_patient(db:Session,patient_id:int):
    db_patient=db.query(model_patient.Patient).filter(model_patient.Patient.id==patient_id).first()
    if db_patient is None:
        return None
    return db_patient

def check_lab_technician(db:Session,labtechnician_id:int):
    db_lab_technician=db.query(model_labtechnician.LabTechnician).filter(model_labtechnician.LabTechnician.id==labtechnician_id).first()
    if db_lab_technician is None:
        return None
    return db_lab_technician


def get_labtests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_labtest.LabTest).offset(skip).limit(limit).all()


def get_labtest(db: Session, labtest_id: int):
    db_labtest = db.query(model_labtest.LabTest).filter(
        model_labtest.LabTest.id == labtest_id).first()
    if db_labtest is None:
        return None
    return db_labtest


def update_labtest(db: Session, labtest: schema_labtest.LabTestUpdate):
    db_labtest = db.query(model_labtest.LabTest).filter(
        model_labtest.LabTest.id == labtest.id).first()
    if db_labtest is None:
        return None
    for key, value in labtest.model_dump().items():
        setattr(db_labtest, key, value)
    db.commit()
    db.refresh(db_labtest)
    return db_labtest


def delete_labtest(db: Session, labtest_id: int):
    db_labtest = db.query(model_labtest.LabTest).filter(
        model_labtest.LabTest.id == labtest_id).first()
    if db_labtest is None:
        return None
    db.delete(db_labtest)
    db.commit()
    return db_labtest
