from sqlalchemy.orm import Session
from models import labtechnician as model_labtechnician
from schemas import labtechnician as schema_labtechnician
from typing import List


def create_labtechnician(db: Session, labtechnician: schema_labtechnician.LabTechnicianCreate):
    db_labtechnician = model_labtechnician.LabTechnician(
        **labtechnician.model_dump())
    db.add(db_labtechnician)
    db.commit()
    db.refresh(db_labtechnician)
    return db_labtechnician


def get_labtechnicians(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_labtechnician.LabTechnician).offset(skip).limit(limit).all()


def get_labtechnician(db: Session, labtechnician_id: int):
    db_labtechnician = db.query(model_labtechnician.LabTechnician).filter(
        model_labtechnician.LabTechnician.id == labtechnician_id).first()
    if db_labtechnician is None:
        return None
    return db_labtechnician


def update_labtechnician(db: Session, labtechnician: schema_labtechnician.LabTechnicianUpdate):
    db_labtechnician = db.query(model_labtechnician.LabTechnician).filter(
        model_labtechnician.LabTechnician.id == labtechnician.id).first()
    if db_labtechnician is None:
        return None
    for key, value in labtechnician.model_dump().items():
        setattr(db_labtechnician, key, value)
    db.commit()
    db.refresh(db_labtechnician)
    return db_labtechnician


def delete_labtechnician(db: Session, labtechnician_id: int):
    db_labtechnician = db.query(model_labtechnician.LabTechnician).filter(
        model_labtechnician.LabTechnician.id == labtechnician_id).first()
    if db_labtechnician is None:
        return None
    db.delete(db_labtechnician)
    db.commit()
    return db_labtechnician
