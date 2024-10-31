from fastapi import APIRouter, HTTPException
from models.appointments import Appointment
from bulk_database.appointments_db_helper import AppointmentsDbHelper

router = APIRouter()

@router.post("/appointments/")
def create_appointment(appointment: Appointment):
    if AppointmentsDbHelper.insert_appointment(appointment):
        return {"message": "Appointment created successfully!"}, 201
    else:
        raise HTTPException(status_code=500, detail="Error creating appointment")

@router.get("/appointments/")
def get_appointments():
    appointments, success = AppointmentsDbHelper.get_appointments()
    
    if not success:
        raise HTTPException(status_code=500, detail="Error retrieving appointments")
    
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found")
    
    return appointments