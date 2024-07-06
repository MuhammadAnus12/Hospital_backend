from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import department as model_department
from cruds import department as crud_department
from schemas import department as schema_department


router = APIRouter()
tags = ["Department"]

@router.post("/department", response_model=schema_department.Department, tags=tags)
def create_department(department: schema_department.DepartmentCreate, db: Session = Depends(get_db)):
    return crud_department.create_department(db, department)

@router.get("/department/{department_id}", response_model=schema_department.Department, tags=tags)
def read_department(department_id: int, db: Session = Depends(get_db)):
    db_department = crud_department.get_department(db, department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department

@router.get("/departments", response_model=schema_department.Departments, tags=tags)
def read_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    departments = crud_department.get_departments(
        db, skip=skip, limit=limit)
    total_count = db.query(model_department.Department).count()
    return {
        "departments": departments,
        "total_count": total_count
    }

@router.put("/departments", response_model=schema_department.Department, tags=tags)
def update_department(department: schema_department.DepartmentUpdate, db: Session = Depends(get_db)):
    db_department = crud_department.get_department(db, department.id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    db_department = crud_department.update_department(db, department)
    return db_department

@router.delete("/department/{department_id}", tags=tags)
def delete_department(department_id: int, db: Session = Depends(get_db)):
    db_department = crud_department.get_department(db, department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    db_department_in_child=crud_department.check_department_child(db,department_id)
    if db_department_in_child is True:
        raise HTTPException(status_code=404,detail="Department child exist")
    return crud_department.delete_department(db, department_id)

@router.post("/department/search", response_model=schema_department.Department, tags=tags)
def search_department(department: schema_department.SearchDepartment, db: Session = Depends(get_db)):
    db_department = crud_department.search_department(db, department)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department

