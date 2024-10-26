from pydantic import BaseModel
from typing import Optional
from datetime import date

class Appointment(BaseModel):
    appointment_id: Optional[int]
    client_id: int
    appointment_date: date
    treatment: str
    doctor_id: int
