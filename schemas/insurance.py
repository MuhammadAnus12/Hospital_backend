from pydantic import BaseModel
from datetime import date
from typing import List

class InsuranceBase(BaseModel):
    company_name: str
    policy_number: int
    coverage_details: str
    
class InsuranceCreate(InsuranceBase):
    pass

class Insurance(InsuranceBase):
    id: int

    class ConfigDict:
        from_attributes = True

class InsuranceUpdate(InsuranceBase):
    id: int

class InsuranceID(Insurance):
    id: int

    class ConfigDict:
        from_attributes = True

class Insurances(BaseModel):
    insurances: List[Insurance]
    total_count: int