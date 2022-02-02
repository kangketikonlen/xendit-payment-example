import datetime

from typing import Optional
from pydantic import BaseModel


class VirtaccIn(BaseModel):
    bank_code: str
    name: str
    expected_amount: int
    is_closed: Optional[bool] = False
    is_single_use: Optional[bool] = False


class VirtaccXendit(BaseModel):
    external_id: str
    bank_code: str
    name: str
    expected_amount: int
    is_closed: Optional[bool] = False
    is_single_use: Optional[bool] = False
