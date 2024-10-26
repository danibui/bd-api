from pydantic import BaseModel
from typing import Optional
from datetime import date

class MedicalHistory(BaseModel):
    history_id: Optional[int]
    client_id: int
    description: str
    history_date: date
