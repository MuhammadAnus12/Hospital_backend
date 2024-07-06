from sqlalchemy.orm import Session
from models import nurse as model_nurse,department as model_department
from schemas import nurse as schema_nurse
from typing import List


def create_nurse(db: Session, nurse: schema_nurse.NurseCreate):
    db_nurse = model_nurse.Nurse(**nurse.model_dump())
    db.add(db_nurse)
    db.commit()
    db.refresh(db_nurse)
    return db_nurse

def check_department(db:Session,department_id:int):
    db_department=db.query(model_department.Department).filter(model_department.Department.id==department_id).first()
    if db_department is None:
        return None
    return db_department
    

def get_nurses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_nurse.Nurse).offset(skip).limit(limit).all()


def get_nurse(db: Session, nurse_id: int):
    db_nurse = db.query(model_nurse.Nurse).filter(
        model_nurse.Nurse.id == nurse_id).first()
    if db_nurse is None:
        return None
    return db_nurse


def update_nurse(db: Session, nurse: schema_nurse.NurseUpdate):
    db_nurse = db.query(model_nurse.Nurse).filter(
        model_nurse.Nurse.id == nurse.id).first()
    if db_nurse is None:
        return None
    for key, value in nurse.model_dump().items():
        setattr(db_nurse, key, value)
    db.commit()
    db.refresh(db_nurse)
    return db_nurse


def delete_nurse(db: Session, nurse_id: int):
    db_nurse = db.query(model_nurse.Nurse).filter(
        model_nurse.Nurse.id == nurse_id).first()
    if db_nurse is None:
        return None
    db.delete(db_nurse)
    db.commit()
    return db_nurse


def search_nurse(db: Session, nurse: schema_nurse.SearchNurse):
    db_nurse = db.query(model_nurse.Nurse).filter
    (model_nurse.Nurse.first_name == nurse.first_name).filter
    (model_nurse.Nurse.last_name ==nurse.last_name).filter
    (model_nurse.Nurse.shift == nurse.shift).first()
    if db_nurse is None:
        return None
    return db_nurse

