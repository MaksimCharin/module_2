import os
from typing import Any, Dict, Optional

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

URL_USD = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
URL_EUR = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1"

payload: Dict[str, Any] = {}
headers = {"apikey": API_KEY}


def convert_to_rub(code: str) -> Optional[float]:
    """Функция делает запрос на внешний API и получает оттуда актуальные данные по крусу валют
    возвращает необходимое значение"""
    if code == "EUR":
        response_usd = requests.request("GET", URL_USD, headers=headers, data=payload)
        result = response_usd.json()
        value = result.get("result", None)
        return float(value) if value is not None else None
    elif code == "USD":
        response_eur = requests.request("GET", URL_EUR, headers=headers, data=payload)
        result = response_eur.json()
        value = result.get("result", None)
        return float(value) if value is not None else None
    else:
        return None
