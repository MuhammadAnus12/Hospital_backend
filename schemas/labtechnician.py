from pydantic import BaseModel
from datetime import date
from typing import List

class LabTechnicianBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    
class LabTechnicianCreate(LabTechnicianBase):
    pass

class LabTechnician(LabTechnicianBase):
    id :int

    class ConfigDict:
        from_attributes = True

class LabTechnicianUpdate(LabTechnicianBase):
    id: int

class LabTechnicianID(LabTechnician):
    id: int

    class ConfigDict:
        from_attributes = True

class LabTechnicians(BaseModel):
    labtechnicians: List[LabTechnician]
    total_count: int
