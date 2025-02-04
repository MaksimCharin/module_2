import json
import os

from src.external_api import convert_to_rub

current_dir = os.path.dirname(os.path.abspath(__file__))
JSON_DATA = os.path.join(current_dir, '..', 'data', 'operations.json')


def load_transactions(file_path):
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                return []
            return data
    except json.JSONDecodeError:
        return []


transactions = load_transactions(JSON_DATA)
print(transactions)


def gen_transactions(transactions):
    for transaction in transactions:
        yield transaction


transaction = gen_transactions(transactions)


def get_transaction_amount(transaction: dict) -> str:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит конвертации суммы операции в рубли"""
    amount = transaction.get('operationAmount', {}).get('amount')
    code = transaction.get('operationAmount', {}).get('currency', {}).get('code')
    id = transaction.get('id', {})

    if code == 'RUB':
        return f"Сумма транзакции: {amount} руб. Код валюты: {code}, id: {id}"
    elif code in ["USD", "EUR"]:
        exchange_rate = convert_to_rub(code)
        if exchange_rate == None:
            return "Что-то пошло не так, данные с API не подгрузились"
        result = round(float(amount) * exchange_rate, 4)
        return f"Сумма транзакции: {result} руб. Код валюты: {code}, id: {id}"
    else:
        raise ValueError(f"Unsupported currency: {code}")