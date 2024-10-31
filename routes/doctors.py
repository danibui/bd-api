from fastapi import APIRouter, HTTPException
from models.doctors import Doctor
from bulk_database.doctors_db_helper import DoctorsDbHelper

router = APIRouter()

@router.post("/doctors/")
def create_doctor(doctor: Doctor):
    if DoctorsDbHelper.insert_doctor(doctor):
        return {"message": "Doctor created successfully!"}, 201
    else:
        raise HTTPException(status_code=500, detail="Error creating doctor")


@router.get("/doctors/")
def get_doctors():
    success = DoctorsDbHelper.get_doctors()
    
    if not success:
        raise HTTPException(status_code=500, detail="Error retrieving doctors")
    
    return success
