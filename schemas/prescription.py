from pydantic import BaseModel
from typing import List

class PrescriptionBase(BaseModel):
    treatment_id: int
    medication_id: int
    dosage: str
    frequency: str
    duration: str

class PrescriptionCreate(PrescriptionBase):
    pass

class Prescription(PrescriptionBase):
    id: int

    class ConfigDict:
        from_attributes = True

class PrescriptionUpdate(PrescriptionBase):
    id: int

class PrescriptionID(Prescription):
    id: int

    class ConfigDict:
        from_attributes = True

class Prescriptions(BaseModel):
    prescriptions: List[Prescription]
    total_count: int

