from pydantic import BaseModel
from datetime import date
from typing import List

class NurseBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    shift: str
    department_id: int

class NurseCreate(NurseBase):
    pass

class Nurse(NurseBase):
    id :int

    class ConfigDict:
        from_attributes = True

class NurseUpdate(NurseBase):
    id: int

class NurseID(Nurse):
    id: int

    class ConfigDict:
        from_attributes = True

class Nurses(BaseModel):
    nurses: List[Nurse]
    total_count: int

class SearchNurse(BaseModel):
    first_name: str
    last_name: str
    shift: str
