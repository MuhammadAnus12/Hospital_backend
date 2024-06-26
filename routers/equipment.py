from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import equipment as model_equipment
from cruds import equipment as crud_equipment
from schemas import equipment as schema_equipment


router = APIRouter()
tags = ["Equipment"]

@router.post("/equipment", response_model=schema_equipment.Equipment, tags=tags)
def create_equipment(equipment: schema_equipment.EquipmentCreate, db: Session = Depends(get_db)):
    return crud_equipment.create_equipment(db, equipment)

@router.get("/equipment/{equipment_id}", response_model=schema_equipment.Equipment, tags=tags)
def read_equipment(equipment_id: int, db: Session = Depends(get_db)):
    db_equipment = crud_equipment.get_equipment(db, equipment_id)
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return db_equipment

@router.get("/equipments", response_model=schema_equipment.Equipments, tags=tags)
def read_equipments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    equipments = crud_equipment.get_equipments(db, skip=skip, limit=limit)
    total_count = db.query(model_equipment.Equipment).count()
    return {
        "equipments": equipments,
        "total_count": total_count
    }

@router.put("/equipments", response_model=schema_equipment.Equipment, tags=tags)
def update_equipment(equipment: schema_equipment.EquipmentUpdate, db: Session = Depends(get_db)):
    db_equipment = crud_equipment.get_equipment(db, equipment.id)
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    db_equipment = crud_equipment.update_equipment(db, equipment)
    return db_equipment

@router.delete("/equipment/{equipment_id}", tags=tags)
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    db_equipment = crud_equipment.get_equipment(db, equipment_id)
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return crud_equipment.delete_equipment(db, equipment_id)

