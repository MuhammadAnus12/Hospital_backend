from pydantic import BaseModel
from datetime import date
from typing import List


class PatientBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    gender: str
    address: str
    phone_number: str
    email: str
    emergency_id: int
    insurance_id: int
    medical_record_id: int


class PatientCreate(PatientBase):
    pass


class Patient(PatientBase):
    id: int

    class ConfigDict:
        from_attributes = True


class PatientUpdate(PatientBase):
    id: int


class PatientID(Patient):
    id: int

    class ConfigDict:
        from_attributes = True


class Patients(BaseModel):
    patients: List[Patient]
    total_count: int

class SearchPatient(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date