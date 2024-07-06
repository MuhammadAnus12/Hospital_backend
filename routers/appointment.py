from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import appointment as model_appointment
from cruds import appointment as crud_appointment
from schemas import appointment as schema_appointment


router = APIRouter()
tags = ["Appointment"]


@router.post("/appointment", response_model=schema_appointment.Appointment, tags=tags)
def create_appointment(appointment: schema_appointment.AppointmentCreate, db: Session = Depends(get_db)):
    db_doctor=crud_appointment.check_doctor(db,appointment.doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404,detail="Doctor not found")
    db_patient=crud_appointment.check_patient(db,appointment.patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404,detail="Patient not found")
    return crud_appointment.create_appointment(db, appointment)


@router.get("/appointment/{appointment_id}", response_model=schema_appointment.Appointment, tags=tags)
def read_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appointment = crud_appointment.get_appointment(db, appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment


@router.get("/appointments", response_model=schema_appointment.Appointments, tags=tags)
def read_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointments = crud_appointment.get_appointments(
        db, skip=skip, limit=limit)
    total_count = db.query(model_appointment.Appointment).count()
    return {
        "appointments": appointments,
        "total_count": total_count
    }


@router.put("/appointment", response_model=schema_appointment.Appointment, tags=tags)
def update_appointment(appointment: schema_appointment.AppointmentUpdate, db: Session = Depends(get_db)):
    db_appointment = crud_appointment.get_appointment(db, appointment.id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    db_doctor=crud_appointment.check_doctor(db,appointment.doctor_id)
    if db_doctor is None:
        raise HTTPException(status_code=404,detail="Doctor not found")
    db_patient=crud_appointment.check_patient(db,appointment.patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404,detail="Patient not found")
    db_appointment = crud_appointment.update_appointment(db, appointment)
    return db_appointment


@router.delete("/appointment/{appointment_id}", tags=tags)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    db_appointment = crud_appointment.get_appointment(db, appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return crud_appointment.delete_appointment(db, appointment_id)


@router.post("/appointment/search", response_model=schema_appointment.Appointment, tags=tags)
def search_appointment(appointment: schema_appointment.SearchAppointment, db: Session = Depends(get_db)):
    db_appointment = crud_appointment.search_appointment(db, appointment)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment
