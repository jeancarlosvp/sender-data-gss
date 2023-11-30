from pydantic import BaseModel
from typing import Optional

class DataPayments(BaseModel):
    date_payment: str
    dni: Optional[str] = None
    total: Optional[float] = None
    bank: Optional[int] = None
    mode_payment: Optional[str] = None
    operation_code: Optional[str] = None
    card_number: Optional[str] = None
