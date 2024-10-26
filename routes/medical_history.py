from fastapi import APIRouter, HTTPException
from models.medical_history import MedicalHistory
from database import get_db_connection

router = APIRouter()

@router.post("/medical_history/")
def create_medical_history(history: MedicalHistory):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
        INSERT INTO medical_history (client_id, description, history_date)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (history.client_id, history.description, history.history_date))
    conn.commit()
    cursor.close()
    conn.close()
    
    return {"message": "Medical history entry created successfully!"}

@router.get("/medical_history/")
def get_medical_history():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM medical_history"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if not result:
        raise HTTPException(status_code=404, detail="No medical history found")
    
    return result
