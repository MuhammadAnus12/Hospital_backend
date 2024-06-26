from pydantic import BaseModel
from datetime import date
from typing import List

class TreatmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    diagnosis: str
    treatment_plan: str
    start_date: date
    end_date: date

class TreatmentCreate(TreatmentBase):
    pass

class Treatment(TreatmentBase):
    id: int

    class ConfigDict:
        from_attributes = True

class TreatmentUpdate(TreatmentBase):
    id: int

class TreatmentID(Treatment):
    id: int

    class ConfigDict:
        from_attributes = True

class Treatments(BaseModel):
    treatments: List[Treatment]
    total_count: int

class SearchTreatment(BaseModel):
    diagnosis: str
    treatment_plan: str