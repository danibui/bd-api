from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

class Treatment(BaseModel):
    treatment_id: Optional[int]
    appointment_id: int
    treatment_type: str
    cost: Decimal
    treatment_date: date
