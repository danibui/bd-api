from fastapi import APIRouter, HTTPException
from models.payments import Payment
from database import get_db_connection

router = APIRouter()

@router.post("/payments/")
def create_payment(payment: Payment):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """
        INSERT INTO payments (appointment_id, amount, payment_date, payment_method)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (payment.appointment_id, payment.amount, payment.payment_date, payment.payment_method))
    conn.commit()
    cursor.close()
    conn.close()
    
    return {"message": "Payment created successfully!"}

@router.get("/payments/")
def get_payments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT * FROM payments"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if not result:
        raise HTTPException(status_code=404, detail="No payments found")
    
    return result
