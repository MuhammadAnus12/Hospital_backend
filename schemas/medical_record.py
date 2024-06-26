from pydantic import BaseModel
from datetime import date
from typing import List

class MedicalRecordBase(BaseModel):
    details: str
    created_date: date

class MedicalRecordCreate(MedicalRecordBase):
    pass

class MedicalRecord(MedicalRecordBase):
    id: int

    class ConfigDict:
        from_attributes = True

class MedicalRecordUpdate(MedicalRecordBase):
    id: int

class MedicalRecordID(MedicalRecord):
    id: int

    class ConfigDict:
        from_attributes = True

class MedicalRecords(BaseModel):
    medical_records: List[MedicalRecord]
    total_count: int
