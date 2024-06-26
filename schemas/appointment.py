from pydantic import BaseModel
from datetime import date
from typing import List


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: str
    status: str


class AppointmentCreate(AppointmentBase):
    pass


class Appointment(AppointmentBase):
    id: int

    class ConfigDict:
        from_attributes = True

class AppointmentUpdate(AppointmentBase):
    id: int

class AppointmentID(Appointment):
    id: int

    class ConfigDict:
        from_attributes = True

class Appointments(BaseModel):
    appointments: List[Appointment]
    total_count: int

class SearchAppointment(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date
    