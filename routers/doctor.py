from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import doctor as model_doctor
from cruds import doctor as crud_doctor
from schemas import doctor as schema_doctor
from typing import List

router = APIRouter()
tags = ['Doctor']


@router.post('/doctor', response_model=schema_doctor.Doctor, tags=tags)
def create_doctor(doctor: schema_doctor.DoctorCreate, db: Session = Depends(get_db)):
    db_room = crud_doctor.check_room(db, doctor.room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    db_department = crud_doctor.check_department(db, doctor.department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return crud_doctor.create_doctor(db, doctor)


@router.get('/doctor/{doctor_id}', response_model=schema_doctor.Doctor, tags=tags)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud_doctor.get_doctor(db, doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail='Doctor not found')
    return db_doctor


@router.get('/doctors', response_model=schema_doctor.Doctors, tags=tags)
def get_doctors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    doctors = crud_doctor.get_doctors(db, skip, limit)
    total_count = db.query(model_doctor.Doctor).count()
    return {
        'doctors': doctors,
        'total_count': total_count
    }


@router.put('/doctors', response_model=schema_doctor.Doctor, tags=tags)
def update_doctor(doctor: schema_doctor.DoctorUpdate, db: Session = Depends(get_db)):
    db_doctor = crud_doctor.get_doctor(db, doctor.id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail='Doctor not found')
    db_room = crud_doctor.check_room(db, doctor.room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    db_department = crud_doctor.check_department(db, doctor.department_id)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    db_doctor = crud_doctor.update_doctor(db, doctor)
    return db_doctor


@router.delete('/doctor/{doctor_id}', tags=tags)
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    db_doctor = crud_doctor.get_doctor(db, doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail='Doctor not found')
    db_doctor_in_child = crud_doctor.check_doctor_in_child(db, doctor_id)
    if db_doctor_in_child is True:
        raise HTTPException(status_code=404, detail="Doctor Exist in Child")
    return crud_doctor.delete_doctor(db, doctor_id)


@router.post('/doctor/search', response_model=schema_doctor.Doctor, tags=tags)
def search_doctor(doctor: schema_doctor.SearchDoctor, db: Session = Depends(get_db)):
    db_doctor = crud_doctor.search_doctor(db, doctor)
    if db_doctor is None:
        raise HTTPException(status_code=404, detail='Doctor not found')
    return db_doctor
