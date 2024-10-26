from fastapi import APIRouter, HTTPException, Depends
from models.appointments import Appointment
from database import get_db_connection

router = APIRouter()

@router.post("/appointments/")
def create_appointment(appointment: Appointment):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO appointments (client_id, appointment_date, treatment, doctor_id) 
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (appointment.client_id, appointment.appointment_date, appointment.treatment, appointment.doctor_id))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Appointment created successfully!"}

@router.get("/appointments/")
def get_appointments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM appointments"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    if not result:
        raise HTTPException(status_code=404, detail="No appointments found")
    
    return result
