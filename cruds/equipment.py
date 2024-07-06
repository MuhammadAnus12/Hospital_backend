from sqlalchemy.orm import Session
from models import equipment as model_equipment,room as model_room
from schemas import equipment as schema_equipment
from typing import List

def create_equipment(db: Session, equipment: schema_equipment.EquipmentCreate):
    db_equipment = model_equipment.Equipment(**equipment.model_dump())
    db.add(db_equipment)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment

def get_equipments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_equipment.Equipment).offset(skip).limit(limit).all()

def check_room(db:Session,room_id:int):
    db_room=db.query(model_room.Room).filter(model_room.Room.id==room_id).first()
    if db_room is None:
        return None
    return db_room

def get_equipment(db: Session, equipment_id: int):
    db_equipment = db.query(model_equipment.Equipment).filter(
        model_equipment.Equipment.id == equipment_id).first()
    if db_equipment is None:
        return None
    return db_equipment

def update_equipment(db: Session, equipment: schema_equipment.EquipmentUpdate):
    db_equipment = db.query(model_equipment.Equipment).filter(
        model_equipment.Equipment.id == equipment.id).first()
    if db_equipment is None:
        return None
    for key, value in equipment.model_dump().items():
        setattr(db_equipment, key, value)
    db.commit()
    db.refresh(db_equipment)
    return db_equipment

def delete_equipment(db: Session, equipment_id: int):
    db_equipment = db.query(model_equipment.Equipment).filter(
        model_equipment.Equipment.id == equipment_id).first()
    if db_equipment is None:
        return None
    db.delete(db_equipment)
    db.commit()
    return db_equipment
