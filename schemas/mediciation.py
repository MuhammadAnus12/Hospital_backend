from pydantic import BaseModel
from datetime import date
from typing import List

class MedicationBase(BaseModel):
    name: str
    manufacturer: str
    expiry_date: date
    quantity_in_stock: int
    price: int

class MedicationCreate(MedicationBase):
    pass

class Medication(MedicationBase):
    id: int

    class ConfigDict:
        from_attributes = True

class MedicationUpdate(MedicationBase):
    id: int

class MedicationID(Medication):
    id: int

    class ConfigDict:
        from_attributes = True

class Medications(BaseModel):
    medications: List[Medication]
    total_count: int

