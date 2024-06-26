from sqlalchemy.orm import Session
from models import emergency as model_emergency
from schemas import emergency as schema_emergency
from typing import List

def create_emergency(db: Session, emergency: schema_emergency.EmergencyCreate):
    db_emergency = model_emergency.Emergency(**emergency.dict())
    db.add(db_emergency)
    db.commit()
    db.refresh(db_emergency)
    return db_emergency

def get_emergencies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_emergency.Emergency).offset(skip).limit(limit).all()

def get_emergency(db: Session, emergency_id: int):
    db_emergency = db.query(model_emergency.Emergency).filter(
        model_emergency.Emergency.id == emergency_id).first()
    if db_emergency is None:
        return None
    return db_emergency

def update_emergency(db: Session, emergency: schema_emergency.EmergencyUpdate):
    db_emergency = db.query(model_emergency.Emergency).filter(
        model_emergency.Emergency.id == emergency.id).first()
    if db_emergency is None:
        return None
    for key, value in emergency.model_dump().items():
        setattr(db_emergency, key, value)
    db.commit()
    db.refresh(db_emergency)
    return db_emergency

def delete_emergency(db: Session, emergency_id: int):
    db_emergency = db.query(model_emergency.Emergency).filter(
        model_emergency.Emergency.id == emergency_id).first()
    if db_emergency is None:
        return None
    db.delete(db_emergency)
    db.commit()
    return db_emergency
