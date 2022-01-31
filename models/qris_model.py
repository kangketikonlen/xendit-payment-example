from pydantic import BaseModel


class QrcodeIn(BaseModel):
    amount: int = 100000
