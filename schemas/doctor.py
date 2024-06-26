from pydantic import BaseModel
from datetime import date
from typing import List

class DoctorBase(BaseModel):
    first_name: str
    last_name: str
    specialty: str
    phone_number: str
    email: str
    department_id: int
    room_id: int


class DoctorCreate(DoctorBase):
    pass


class Doctor(DoctorBase):
    id: int

    class ConfigDict:
        from_attributes = True


class DoctorUpdate(DoctorBase):
    id: int


class DoctorID(Doctor):
    id: int

    class ConfigDict:
        from_attributes = True


class Doctors(BaseModel):
    doctors: List[Doctor]
    total_count: int

class SearchDoctor(BaseModel):
    first_name: str
    last_name: str
    specialty: str

