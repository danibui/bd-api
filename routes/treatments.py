from fastapi import APIRouter, HTTPException
from models.treatments import Treatment
from bulk_database.treatments_db_helper import TreatmentsDbHelper

router = APIRouter()

@router.post("/treatments/")
def create_treatment(treatment: Treatment):
    TreatmentsDbHelper.create_treatment(treatment)
    return {"message": "Treatment created successfully!"}

@router.get("/treatments/")
def get_treatments():
    result = TreatmentsDbHelper.get_all_treatments()
    if not result:
        raise HTTPException(status_code=404, detail="No treatments found")
    return result