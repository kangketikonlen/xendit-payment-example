from fastapi import APIRouter, HTTPException, exceptions

from utils.message_util import MessageOut, output_message
from models.qris_model import QrcodeIn
from services.qris_service import create_qris, get_qris

router = APIRouter()


@router.get("/{external_id}", response_model=MessageOut)
async def get_qris_payment(external_id: str):
    response = await get_qris(external_id)
    return output_message(response.json(), "Api Call Success!")


@router.post("/", response_model=MessageOut)
async def create_qris_payment(data: QrcodeIn):
    response = await create_qris(data.amount)
    return output_message(response.json(), "Api Call Success!")
