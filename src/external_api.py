import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

URL_USD = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
URL_EUR = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1"

payload = {}
headers = {"apikey": API_KEY}


def convert_to_rub(code):
    if code == "EUR":
        response_usd = requests.request("GET", URL_USD, headers=headers, data=payload)
        result = response_usd.json()

        return result.get("result", None)
    elif code == "USD":
        response_eur = requests.request("GET", URL_EUR, headers=headers, data=payload)
        result = response_eur.json()
        return result.get("result", None)
