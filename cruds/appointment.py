from sqlalchemy.orm import Session
from models import (appointment as model_appointment,
                patient as model_patient,
                doctor as model_doctor)
from schemas import appointment as schema_appointment
from typing import List


def create_appointment(db: Session, appointment: schema_appointment.AppointmentCreate):
    db_appointment = model_appointment.Appointment(**appointment.model_dump())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def check_patient(db:Session,patient_id:int):
    db_patient=db.query(model_patient.Patient).filter(model_patient.Patient.id==patient_id).first()
    if db_patient is None:
        return None
    return db_patient

def check_doctor(db:Session,doctor_id:int):
    db_doctor=db.query(model_doctor.Doctor).filter(model_doctor.Doctor.id==doctor_id).first()
    if db_doctor is None:
        return None
    return db_doctor

def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_appointment.Appointment).offset(skip).limit(limit).all()

def get_appointment(db: Session, appointment_id: int):
    db_appointment = db.query(model_appointment.Appointment).filter(
        model_appointment.Appointment.id == appointment_id).first()
    if db_appointment is None:
        return None
    return db_appointment

def update_appointment(db: Session, appointment: schema_appointment.AppointmentUpdate):
    db_appointment = db.query(model_appointment.Appointment).filter(
        model_appointment.Appointment.id == appointment.id).first()
    if db_appointment is None:
        return None
    for key, value in appointment.model_dump().items():
        setattr(db_appointment, key, value)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def delete_appointment(db: Session, appointment_id: int):
    db_appointment = db.query(model_appointment.Appointment).filter(
        model_appointment.Appointment.id == appointment_id).first()
    if db_appointment is None:
        return None
    db.delete(db_appointment)
    db.commit()
    return db_appointment

def search_appointment(db: Session, appointment: schema_appointment.SearchAppointment):
    db_appointment = db.query(model_appointment.Appointment).filter(model_appointment.Appointment.patient_id == appointment.patient_id).filter(model_appointment.Appointment.doctor_id == appointment.doctor_id).filter(model_appointment.Appointment.appointment_date == appointment.appointment_date).first()
    if db_appointment is None:
        return None
    return db_appointment

