from sqlalchemy.orm import Session
from models import room as model_room
from schemas import room as schema_room
from typing import List


def create_room(db: Session, room: schema_room.RoomCreate):
    db_room = model_room.Room(**room.model_dump())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room


def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_room.Room).offset(skip).limit(limit).all()


def get_room(db: Session, room_id: int):
    db_room = db.query(model_room.Room).filter(
        model_room.Room.id == room_id).first()
    if db_room is None:
        return None
    return db_room


def update_room(db: Session, room: schema_room.RoomUpdate):
    db_room = db.query(model_room.Room).filter(
        model_room.Room.id == room.id).first()
    if db_room is None:
        return None
    for key, value in room.model_dump().items():
        setattr(db_room, key, value)
    db.commit()
    db.refresh(db_room)
    return db_room


def delete_room(db: Session, room_id: int):
    db_room = db.query(model_room.Room).filter(
        model_room.Room.id == room_id).first()
    if db_room is None:
        return None
    db.delete(db_room)
    db.commit()
    return db_room
