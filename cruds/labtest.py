from sqlalchemy.orm import Session
from models import labtest as model_labtest
from schemas import labtest as schema_labtest
from typing import List


def create_labtest(db: Session, labtest: schema_labtest.LabTestCreate):
    db_labtest = model_labtest.LabTest(**labtest.model_dump())
    db.add(db_labtest)
    db.commit()
    db.refresh(db_labtest)
    return db_labtest


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
