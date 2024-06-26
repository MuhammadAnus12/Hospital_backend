from pydantic import BaseModel
from datetime import date
from typing import List

class LabTestBase(BaseModel):
    patient_id: int
    lab_technician_id: int
    test_name: str
    test_date: date
    result: str

class LabTestCreate(LabTestBase):
    pass

class LabTest(LabTestBase):
    id: int

    class ConfigDict:
        from_attributes = True

class LabTestUpdate(LabTestBase):
    id: int

class LabTestID(LabTest):
    id: int

    class ConfigDict:
        from_attributes = True

class LabTests(BaseModel):
    labtests: List[LabTest]
    total_count: int