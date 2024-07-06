from pydantic import BaseModel

class HeadOfDepartmentBase(BaseModel):
    doctor_id:int
    department_id:int
    name:str

class HeadOfDepartmentCreate(HeadOfDepartmentBase):
    pass

class HeadOfDepartment(HeadOfDepartmentBase):
    id :int
    
    class ConfigDict:
        from_attribute = True

class HeadOfDepartments(BaseModel):
    head_of_departments:list[HeadOfDepartment]
    total_count:int