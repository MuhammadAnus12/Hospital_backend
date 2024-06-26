from pydantic import BaseModel
from typing import List

class EmergencyBase(BaseModel):
    contact_name: str
    phone_number: int
    address: str
    relationships: str


class EmergencyCreate(EmergencyBase):
    pass

class Emergency(EmergencyBase):
    id: int

    class ConfigDict:
        from_attributes = True

class EmergencyUpdate(EmergencyBase):
    id: int

class EmergencyID(Emergency):
    id: int

    class ConfigDict:
        from_attributes = True

class Emergencies(BaseModel):
    emergencies: List[Emergency]
    total_count: int


