import os
import uuid
import requests

from dotenv import load_dotenv

load_dotenv()
KEY = os.environ["XENDIT_KEY"]
HEADERS = {"Authorization": f"Basic {KEY}"}
URL = os.environ["QRCODE_URL"]
REF_ID = str(uuid.uuid4()).lower()


async def create_qris(amount):
    data = {
        "external_id": f"qris_ak-{REF_ID}",
        "type": "DYNAMIC",
        "callback_url": "https://my-shop.com/callbacks",
        "amount": amount
    }
    return requests.post(URL, headers=HEADERS, json=data)


async def get_qris(uid):
    return requests.get(f"{URL}/{uid}", headers=HEADERS)
