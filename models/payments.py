from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

class Payment(BaseModel):
    payment_id: Optional[int]
    appointment_id: int
    amount: Decimal
    payment_date: date
    payment_method: str
