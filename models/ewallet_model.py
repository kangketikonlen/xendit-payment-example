from typing import Optional
from pydantic import BaseModel


class PayIn(BaseModel):
    amount: int = 25000
    mobile: Optional[str] = "085161284041"
