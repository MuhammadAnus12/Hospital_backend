from pydantic import BaseModel
from typing import List

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id: int

    class ConfigDict:
        from_attribute = True

class DepartmentUpdate(DepartmentBase):
    id: int

class DepartmentID(Department):
    id: int

    class ConfigDict:
        from_attribute = True

class Departments(BaseModel):
    departments: List[Department]
    total_count: int

class SearchDepartment(BaseModel):
    name: str