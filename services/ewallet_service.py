import os
import uuid
import requests

from dotenv import load_dotenv

load_dotenv()
KEY = os.environ["XENDIT_KEY"]
HEADERS = {"Authorization": f"Basic {KEY}"}
URL = f"{os.environ['XENDIT_URL']}/ewallets/charges"
REF_ID = str(uuid.uuid4()).lower()


def manual_replace(s, char, index):
    return s[:index] + char + s[index + 1:]


async def create_ewallet_payment(channel_code, mobile, amount):
    country_formated_mobile = manual_replace(mobile, '+62', 0)
    if channel_code == "ID_OVO":
        channel_properties = {"mobile_number": country_formated_mobile}
    else:
        channel_properties = {"success_redirect_url": "https://redirect.me/payment"}
    data = {
        "reference_id": f"{channel_code.lower()}_ak-{REF_ID}",
        "currency": "IDR",
        "amount": amount,
        "checkout_method": "ONE_TIME_PAYMENT",
        "channel_code": channel_code,
        "channel_properties": channel_properties,
        "metadata": {
            "branch_area": "PLUIT",
            "branch_city": "JAKARTA"
        }
    }
    return requests.post(URL, headers=HEADERS, json=data)


async def get_ewallet_payment(uid):
    return requests.get(f"{URL}/{uid}", headers=HEADERS)
