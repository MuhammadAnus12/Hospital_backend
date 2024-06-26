from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import room as model_room
from cruds import room as crud_room
from schemas import room as schema_room


router = APIRouter()
tags = ["Room"]

@router.post("/room", response_model=schema_room.Room, tags=tags)
def create_room(room: schema_room.RoomCreate, db: Session = Depends(get_db)):
    return crud_room.create_room(db, room)

@router.get("/room/{room_id}", response_model=schema_room.Room, tags=tags)
def read_room(room_id: int, db: Session = Depends(get_db)):
    db_room = crud_room.get_room(db, room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

@router.get("/rooms", response_model=schema_room.Rooms, tags=tags)
def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud_room.get_rooms(db, skip=skip, limit=limit)
    total_count = db.query(model_room.Room).count()
    return {
        "rooms": rooms,
        "total_count": total_count
    }

@router.put("/room", response_model=schema_room.Room, tags=tags)
def update_room(room: schema_room.RoomUpdate, db: Session = Depends(get_db)):
    db_room = crud_room.get_room(db, room.id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    db_room = crud_room.update_room(db, room)
    return db_room

@router.delete("/room/{room_id}", tags=tags)
def delete_room(room_id: int, db: Session = Depends(get_db)):
    db_room = crud_room.get_room(db, room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return crud_room.delete_room(db, room_id)
