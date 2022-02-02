import os
import uuid
import requests

from dotenv import load_dotenv
from models.virtacc_model import VirtaccXendit

load_dotenv()
KEY = os.environ["XENDIT_KEY"]
HEADERS = {"Authorization": f"Basic {KEY}"}
URL = f"{os.environ['XENDIT_URL']}/callback_virtual_accounts"
REF_ID = str(uuid.uuid4()).lower()


async def create_fva(data):
    reqs = VirtaccXendit(
        **data.dict(),
        external_id=f"va-{data.bank_code.lower()}-{REF_ID}"
    ).dict()
    return requests.post(URL, headers=HEADERS, json=reqs)


async def check_fva(uid):
    return requests.get(f"{URL}/{uid}", headers=HEADERS)
