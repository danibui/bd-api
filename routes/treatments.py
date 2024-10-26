from fastapi import APIRouter, HTTPException
from models.treatments import Treatment
from database import get_db_connection

router = APIRouter()

@router.post("/treatments/")
def create_treatment(treatment: Treatment):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
        INSERT INTO treatments (appointment_id, treatment_type, cost, treatment_date)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (treatment.appointment_id, treatment.treatment_type, treatment.cost, treatment.treatment_date))
    conn.commit()
    cursor.close()
    conn.close()
    
    return {"message": "Treatment created successfully!"}

@router.get("/treatments/")
def get_treatments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM treatments"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if not result:
        raise HTTPException(status_code=404, detail="No treatments found")
    
    return result
