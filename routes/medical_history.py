from fastapi import APIRouter, HTTPException
from models.medical_history import MedicalHistory
from bulk_database.medical_history_db_helper import MedicalHistoryDbHelper

router = APIRouter()

@router.post("/medical_history/")
def create_medical_history(history: MedicalHistory):
    MedicalHistoryDbHelper.create_medical_history(history)
    return {"message": "Medical history entry created successfully!"}

@router.get("/medical_history/")
def get_medical_history():
    result = MedicalHistoryDbHelper.get_all_medical_history()
    if not result:
        raise HTTPException(status_code=404, detail="No medical history found")
    return result