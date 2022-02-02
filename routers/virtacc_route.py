from fastapi import APIRouter, HTTPException, exceptions

from utils.message_util import MessageOut, output_message
from models.virtacc_model import VirtaccIn
from services.virtacc_service import create_fva, check_fva

router = APIRouter()


@router.post("/", response_model=MessageOut)
async def create_virtual_account(data: VirtaccIn):
    response = await create_fva(data)
    return output_message(response.json(), "API Call Success!")


@router.get("/{va_id}", response_model=MessageOut)
async def check_virtual_account(va_id: str):
    response = await check_fva(va_id)
    return output_message(response.json(), "API Call Success!")
