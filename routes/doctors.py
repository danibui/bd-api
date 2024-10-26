from fastapi import APIRouter, HTTPException
from models.doctors import Doctor
from database import get_db_connection

router = APIRouter()

@router.post("/doctors/")
def create_doctor(doctor: Doctor):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
        INSERT INTO doctors (name, specialty, phone, email)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (doctor.name, doctor.specialty, doctor.phone, doctor.email))
    conn.commit()
    cursor.close()
    conn.close()
    
    return {"message": "Doctor created successfully!"}

@router.get("/doctors/")
def get_doctors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM doctors"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if not result:
        raise HTTPException(status_code=404, detail="No doctors found")
    
    return result
