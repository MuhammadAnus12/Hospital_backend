from sqlalchemy.orm import Session
from models import (department as model_department,
                    doctor as model_doctor,
                    nurse as model_nurse,
                    room as model_room,
                    head_of_department as model_head_of_department)
from schemas import department as schema_department
from typing import List


def create_department(db: Session, department: schema_department.DepartmentCreate):
    db_department = model_department.Department(**department.model_dump())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department


def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_department.Department).offset(skip).limit(limit).all()


def get_department(db: Session, department_id: int):
    db_department = db.query(model_department.Department).filter(
        model_department.Department.id == department_id).first()
    if db_department is None:
        return None
    return db_department


def update_department(db: Session, department: schema_department.DepartmentUpdate):
    db_department = db.query(model_department.Department).filter(
        model_department.Department.id == department.id).first()
    if db_department is None:
        return None
    for key, value in department.model_dump().items():
        setattr(db_department, key, value)
    db.commit()
    db.refresh(db_department)
    return db_department


def delete_department(db: Session, department_id: int):
    db_department = db.query(model_department.Department).filter(
        model_department.Department.id == department_id).first()
    if db_department is None:
        return None
    db.delete(db_department)
    db.commit()
    return db_department


def search_department(db: Session, department: schema_department.SearchDepartment):
    db_department = db.query(model_department.Department).filter(
        model_department.Department.name == department.name).first()
    if db_department is None:
        return None
    return db_department


def check_department_child(db: Session, department_id: int) -> bool:
    if db.query(model_doctor.Doctor).filter(model_doctor.Doctor.department_id == department_id).first():
        return True
    if db.query(model_nurse.Nurse).filter(model_nurse.Nurse.department_id == department_id).first():
        return True
    if db.query(model_room.Room).filter(model_room.Room.department_id == department_id).first():
        return True
    if db.query(model_head_of_department.HeadOfDepartment).filter(model_head_of_department.HeadOfDepartment.department_id == department_id).first():
        return True
    return False
