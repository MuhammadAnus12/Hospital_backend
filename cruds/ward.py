from sqlalchemy.orm import Session
from models import ward as model_ward
from schemas import ward as schema_ward
from typing import List

def create_ward(db: Session, ward: schema_ward.WardCreate):
    db_ward = model_ward.Ward(**ward.model_dump())
    db.add(db_ward)
    db.commit()
    db.refresh(db_ward)
    return db_ward

def get_wards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_ward.Ward).offset(skip).limit(limit).all()

def get_ward(db: Session, ward_id: int):
    db_ward = db.query(model_ward.Ward).filter(
        model_ward.Ward.id == ward_id).first()
    if db_ward is None:
        return None
    return db_ward

def update_ward(db: Session, ward: schema_ward.WardUpdate):
    db_ward = db.query(model_ward.Ward).filter(
        model_ward.Ward.id == ward.id).first()
    if db_ward is None:
        return None
    for key, value in ward.model_dump().items():
        setattr(db_ward, key, value)
    db.commit()
    db.refresh(db_ward)
    return db_ward

def delete_ward(db: Session, ward_id: int):
    db_ward = db.query(model_ward.Ward).filter(
        model_ward.Ward.id == ward_id).first()
    if db_ward is None:
        return None
    db.delete(db_ward)
    db.commit()
    return db_ward