from pydantic import BaseModel
from datetime import date
from typing import List


class EquipmentBase(BaseModel):
    name: str
    manufacturer: str
    purchase_date: date
    maintenance_date: date
    status: str
    room_id: int


class EquipmentCreate(EquipmentBase):
    pass


class EquipmentUpdate(EquipmentBase):
    id: int


class Equipment(EquipmentBase):
    id: int

    class ConfigDict:
        from_attributes = True

class EquipmentID(Equipment):
    id: int

    class ConfigDict:
        from_attributes = True

class Equipments(BaseModel):
    equipments: List[Equipment]
    total_count: int

