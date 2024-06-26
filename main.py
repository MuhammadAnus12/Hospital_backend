from fastapi import FastAPI
from database import Base,  engine
from routers import (patient, doctor, nurse, 
                     receptionist,appointment, 
                     department, treatment,
                     prescription,mediciation,labtest,
                     labtechnician,invoice,
                     payment,room,ward,
                     supplier,equipment,medical_record,
                     insurance,emergency)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(patient.router)
app.include_router(doctor.router)
app.include_router(nurse.router)
app.include_router(receptionist.router)
app.include_router(appointment.router)
app.include_router(department.router)
app.include_router(treatment.router)
app.include_router(prescription.router)
app.include_router(mediciation.router)
app.include_router(labtest.router)
app.include_router(labtechnician.router)
app.include_router(invoice.router)
app.include_router(payment.router)
app.include_router(room.router)
app.include_router(ward.router)
app.include_router(supplier.router)
app.include_router(equipment.router)
app.include_router(medical_record.router)
app.include_router(insurance.router)
app.include_router(emergency.router)


