from pydantic import BaseModel
from typing import Optional

class Doctor(BaseModel):
    doctor_id: Optional[int]
    name: str
    specialty: str
    phone: str
    email: str
