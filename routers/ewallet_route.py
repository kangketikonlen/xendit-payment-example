from fastapi import APIRouter, HTTPException, exceptions

from utils.message_util import MessageOut, output_message
from services.ewallet_service import create_ewallet_payment, get_ewallet_payment
from models.ewallet_model import PayIn

router = APIRouter()


@router.get("/{charges_id}", response_model=MessageOut)
async def get_payment_detail(charges_id: str):
    response = await get_ewallet_payment(charges_id)
    return output_message(response.json(), "Api Call Success")


@router.post("/ovo", response_model=MessageOut)
async def create_ovo_payment(data: PayIn):
    channel_code = "ID_OVO"
    response = await create_ewallet_payment(channel_code, data.mobile, data.amount)
    return output_message(response.json(), "Api Call Success")


@router.post("/shopeepay", response_model=MessageOut)
async def create_shopeepay_payment(data: PayIn):
    channel_code = "ID_SHOPEEPAY"
    response = await create_ewallet_payment(channel_code, data.mobile, data.amount)
    return output_message(response.json(), "Api Call Success")


@router.post("/dana", response_model=MessageOut)
async def create_dana_payment(data: PayIn):
    channel_code = "ID_DANA"
    response = await create_ewallet_payment(channel_code, data.mobile, data.amount)
    return output_message(response.json(), "Api Call Success")


@router.post("/link-aja", response_model=MessageOut)
async def create_link_aja_payment(data: PayIn):
    channel_code = "ID_LINKAJA"
    response = await create_ewallet_payment(channel_code, data.mobile, data.amount)
    return output_message(response.json(), "Api Call Success")
