from sqlalchemy.orm import Session
from models import receptionist as model_receptionist
from schemas import receptionist as schema_receptionist
from typing import List


def create_receptionist(db: Session, receptionist: schema_receptionist.ReceptionistCreate):
    db_receptionist = model_receptionist.Receptionist(
        **receptionist.model_dump())
    db.add(db_receptionist)
    db.commit()
    db.refresh(db_receptionist)
    return db_receptionist


def get_receptionists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_receptionist.Receptionist).offset(skip).limit(limit).all()


def get_receptionist(db: Session, receptionist_id: int):
    db_receptionist = db.query(model_receptionist.Receptionist).filter(
        model_receptionist.Receptionist.id == receptionist_id).first()
    if db_receptionist is None:
        return None
    return db_receptionist


def update_receptionist(db: Session, receptionist_id: int, receptionist: schema_receptionist.ReceptionistUpdate):
    db_receptionist = db.query(model_receptionist.Receptionist).filter(
        model_receptionist.Receptionist.id == receptionist_id).first()
    if db_receptionist is None:
        return None
    for key, value in receptionist.model_dump().items():
        setattr(db_receptionist, key, value)
    db.commit()
    db.refresh(db_receptionist)
    return db_receptionist


def delete_receptionist(db: Session, receptionist_id: int):
    db_receptionist = db.query(model_receptionist.Receptionist).filter(
        model_receptionist.Receptionist.id == receptionist_id).first()
    if db_receptionist is None:
        return None
    db.delete(db_receptionist)
    db.commit()
    return db_receptionist


def search_receptionist(db: Session, receptionist: schema_receptionist.SearchReceptionist):
    db_receptionist = db.query(model_receptionist.Receptionist).filter(model_receptionist.Receptionist.first_name == receptionist.first_name).filter(
        model_receptionist.Receptionist.last_name == receptionist.last_name).filter(model_receptionist.Receptionist.shift == receptionist.shift).first()
    if db_receptionist is None:
        return None
    return db_receptionist
