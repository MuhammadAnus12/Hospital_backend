from sqlalchemy.orm import Session
from models import (doctor as model_doctor,
                    room as model_room, department as model_department,
                    appointment as model_appointment, treatment as model_treatment
                    )
from schemas import doctor as schema_doctor
from typing import List


def create_doctor(db: Session, doctor: schema_doctor.DoctorCreate):
    db_doctor = model_doctor.Doctor(**doctor.model_dump())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def check_room(db: Session, room_id: int):
    db_room = db.query(model_room.Room).filter(
        model_room.Room.id == room_id).first()
    if db_room is None:
        return None
    return db_room


def check_department(db: Session, department_id: int):
    db_department = db.query(model_department.Department).filter(
        model_department.Department.id == department_id).first()
    if db_department is None:
        return None
    return db_department


def get_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(model_doctor.Doctor).filter(
        model_doctor.Doctor.id == doctor_id).first()
    if db_doctor is None:
        return None
    return db_doctor


def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model_doctor.Doctor).offset(skip).limit(limit).all()


def update_doctor(db: Session, doctor: schema_doctor.DoctorUpdate):
    db_doctor = db.query(model_doctor.Doctor).filter(
        model_doctor.Doctor.id == doctor.id).first()
    if db_doctor is None:
        return None
    for key, value in doctor.model_dump().items():
        setattr(db_doctor, key, value)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def delete_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(model_doctor.Doctor).filter(
        model_doctor.Doctor.id == doctor_id).first()
    if db_doctor is None:
        return None
    db.delete(db_doctor)
    db.commit()
    return db_doctor


def search_doctor(db: Session, doctor: schema_doctor.SearchDoctor):
    db_doctor = db.query(model_doctor.Doctor).filter(model_doctor.Doctor.first_name == doctor.first_name).filter(
        model_doctor.Doctor.last_name == doctor.last_name).filter(model_doctor.Doctor.specialty == doctor.specialty).first()
    if db_doctor is None:
        return None
    return db_doctor


def check_doctor_in_child(db: Session, doctor_id: int) -> bool:
    if db.query(model_appointment.Appointment).filter(model_appointment.Appointment.doctor_id == doctor_id).first():
        return True
    if db.query(model_treatment.Treatment).filter(model_treatment.Treatment.doctor_id == doctor_id).first():
        return True
    return False
