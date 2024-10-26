from pydantic import BaseModel
from typing import Optional
from datetime import date

class Client(BaseModel):
    client_id: Optional[int]
    name: str
    phone: str
    email: str
    start_date: date
    end_date: Optional[date]
