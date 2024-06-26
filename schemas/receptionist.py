from pydantic import BaseModel
from typing import List

class ReceptionistBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    shift: str

class ReceptionistCreate(ReceptionistBase):
    pass


class Receptionist(ReceptionistBase):
    id: int

    class ConfigDict:
        from_attributes = True

class ReceptionistUpdate(ReceptionistBase):
    id: int

class ReceptionistID(Receptionist):
    id: int

    class ConfigDict:
        from_attributes = True

class Receptionists(BaseModel):
    receptionists: List[Receptionist]
    total_count: int


class SearchReceptionist(BaseModel):
    first_name: str
    last_name: str
    shift: str