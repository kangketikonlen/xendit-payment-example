import os
import json

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
        return json.loads(callback_data.decode('utf8').replace("'", '"'))


@router.post("/virtual-account-paid")
async def callback_virtual_account_paid(reqs: Request):
    if reqs.headers.get('x-callback-token') == CB_TOKEN:
        callback_data = await reqs.body()
        return json.loads(callback_data.decode('utf8').replace("'", '"'))


@router.post("/ewallet-payment-status")
async def callback_ewallet_payment_status(reqs: Request):
    if reqs.headers.get('x-callback-token') == CB_TOKEN:
        callback_data = await reqs.body()
        return json.loads(callback_data.decode('utf8').replace("'", '"'))
