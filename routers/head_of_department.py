from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from models import head_of_department as model_head_of_department
from schemas import  head_of_department as schema_head_of_department
from cruds import head_of_department as crud_head_of_department
from database import get_db

router=APIRouter()
tags=["Head Of Department"]


@router.post("/head_of_department", response_model=schema_head_of_department.HeadOfDepartment, 
             tags=tags)
def create_department(head_of_department:schema_head_of_department.HeadOfDepartmentCreate, db: Session = Depends(get_db)):
    db_department=crud_head_of_department.check_department(db,head_of_department.department_id)
    if db_department is None:
        raise HTTPException(status_code=404,detail="Department Not found")
    db_doctor=crud_head_of_department.check_doctor(db,head_of_department.doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404,detail="Doctor Not found")
    return crud_head_of_department.create_head_of_department(db, head_of_department)

@router.get("/head_of_department/{head_of_department_id}", response_model=schema_head_of_department.HeadOfDepartment, tags=tags)
def read_head_of_department(head_of_department_id: int, db: Session = Depends(get_db)):
    db_head_of_department = crud_head_of_department.get_head_of_department(db, head_of_department_id)
    if db_head_of_department is None:
        raise HTTPException(status_code=404, detail="Head of Department not found")
    return db_head_of_department

@router.get("/head_of_department", response_model=schema_head_of_department.HeadOfDepartments, tags=tags)
def read_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    departments = crud_head_of_department.get_head_of_departments(
        db, skip=skip, limit=limit)
    total_count = db.query(model_head_of_department.HeadOfDepartment).count()
    return {
        "head_of_departments": departments,
        "total_count": total_count
    }
