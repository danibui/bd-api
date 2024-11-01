from fastapi import APIRouter, HTTPException
from models.payments import Payment
from bulk_database.queries_db_helper import QueriesDbHelper

router = APIRouter()


@router.get("/payments/method/{payment_method}")
def get_payments_by_method(payment_method: str):
    result = QueriesDbHelper.get_payments_by_method(payment_method)
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No payments found for method: {payment_method}"
        )
    return result


@router.get("/payments/with-treatments")
def get_payments_with_treatments():
    result = QueriesDbHelper.get_payments_with_treatments()
    if not result:
        raise HTTPException(
            status_code=404, 
            detail="No payments with treatments found"
        )
    return result


@router.get("/payments/with-treatments-and-clients")
def get_payments_with_treatments_and_clients():
    result = QueriesDbHelper.get_payments_with_treatments_and_clients()
    if not result:
        raise HTTPException(
            status_code=404, 
            detail="No payments with treatments and clients found"
        )
    return result


@router.get("/clients/with-medical-history")
def get_clients_with_medical_history():
    result = QueriesDbHelper.get_clients_with_medical_history()
    if not result:
        raise HTTPException(
            status_code=404, 
            detail="No clients with medical history found"
        )
    return result


@router.get("/appointments/with-doctors")
def get_appointments_with_doctors():
    result = QueriesDbHelper.get_appointments_with_doctors()
    if not result:
        raise HTTPException(
            status_code=404, 
            detail="No appointments with doctors found"
        )
    return result

@router.get("/appointments/treatment/{treatment}")
def get_appointments_by_treatment(treatment: str):
    result = QueriesDbHelper.get_appointments_by_treatment(treatment)
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No appointments found for treatment: {treatment}"
        )
    return result

@router.get("/treatments/type/{treatment_type}")
def get_treatments_by_type(treatment_type: str):
    result = QueriesDbHelper.get_treatments_by_type(treatment_type)
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No treatments found for type: {treatment_type}"
        )
    return result


@router.get("/treatments/min-cost/{min_cost}")
def get_treatments_by_min_cost(min_cost: float):
    result = QueriesDbHelper.get_treatments_by_min_cost(min_cost)
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No treatments found with cost greater than or equal to: {min_cost}"
        )
    return result


@router.get("/treatments/total-cost")
def get_total_treatments_cost():
    result = QueriesDbHelper.get_total_treatments_cost()
    if not result or result['total_cost'] is None:
        raise HTTPException(
            status_code=404, 
            detail="No treatments found or total cost is zero"
        )
    return {"total_cost": float(result['total_cost'])}


@router.get("/medical-history/from-date/{from_date}")
def get_medical_history_from_date(from_date: str):
    result = QueriesDbHelper.get_medical_history_from_date(from_date)
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No medical history found from date: {from_date}"
        )
    return result


@router.get("/doctors/specialty/{specialty}")
def get_doctors_by_specialty(specialty: str):
    result = QueriesDbHelper.get_doctors_by_specialty(specialty)
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No doctors found with specialty: {specialty}"
        )
    return result


@router.get("/clients/email/{email}")
def get_client_by_email(email: str):
    result = QueriesDbHelper.get_client_by_email(email)
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No client found with email: {email}"
        )
    return result


@router.get("/clients/appointments/doctor/{doctor_id}")
def get_clients_appointments_by_doctor(doctor_id: int):
    result = QueriesDbHelper.get_clients_appointments_by_doctor(doctor_id)
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No appointments found for doctor with ID: {doctor_id}"
        )
    return result

@router.get("/payments/client/{client_id}")
def get_payments_by_client_id(client_id: int):
    result = QueriesDbHelper.get_payments_by_client_id(client_id)
    if not result:
        raise HTTPException(
            status_code=404, 
            detail=f"No payments found for client with ID: {client_id}"
        )
    return result