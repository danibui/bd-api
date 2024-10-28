from fastapi import APIRouter, HTTPException
from models.payments import Payment
from bulk_database.payments_db_helper import PaymentsDbHelper

router = APIRouter()

@router.post("/payments/")
def create_payment(payment: Payment):
    PaymentsDbHelper.create_payment(payment)
    return {"message": "Payment created successfully!"}

@router.get("/payments/")
def get_payments():
    result = PaymentsDbHelper.get_all_payments()
    if not result:
        raise HTTPException(status_code=404, detail="No payments found")
    return result