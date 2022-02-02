import os

from fastapi import Request
from fastapi import APIRouter, HTTPException, exceptions

from utils.message_util import MessageOut, output_message
from dotenv import load_dotenv

router = APIRouter()
load_dotenv()
CB_TOKEN = os.environ["XENDIT_CB_TOKEN"]


@router.post("/virtual-account-created")
async def callback_virtual_account_created(reqs: Request):
    if reqs.headers.get('x-callback-token') == CB_TOKEN:
        callback_data = await reqs.body()
        return callback_data


@router.post("/virtual-account-paid")
async def callback_virtual_account_paid(reqs: Request):
    if reqs.headers.get('x-callback-token') == CB_TOKEN:
        callback_data = await reqs.body()
        return callback_data
