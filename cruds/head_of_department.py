from sqlalchemy.orm import Session
from models import (head_of_department as model_head_of_department,
                    doctor as model_doctor,department as model_department)
from schemas import head_of_department as schema_head_of_department

def create_head_of_department(db: Session, head_of_department: schema_head_of_department.HeadOfDepartmentCreate):
    db_head_of_department = model_head_of_department.HeadOfDepartment(**head_of_department.model_dump())
    db.add(db_head_of_department)
    db.commit()
    db.refresh(db_head_of_department)
    return db_head_of_department

def check_doctor(db:Session,doctor_id:int):
    db_doctor=db.query(model_doctor.Doctor).filter(model_doctor.Doctor.id==doctor_id).first()
    if db_doctor is None:
        return None
    return db_doctor

def check_department(db:Session,department_id:int):
    db_department=db.query(model_department.Department).filter(model_department.Department.id==department_id).first()
    if db_department is None:
        return None
    return db_department

def get_head_of_department(db:Session,head_of_department_id:int):
    db_headofdepartment=db.query(model_head_of_department.HeadOfDepartment).filter(
        model_head_of_department.HeadOfDepartment.id==head_of_department_id).first()
    if db_headofdepartment is None:
        return None
    return db_headofdepartment

def get_head_of_departments(db:Session,skip:int=0,limit:int=100):
    return db.query(model_head_of_department.HeadOfDepartment).offset(skip).limit(limit).all()
