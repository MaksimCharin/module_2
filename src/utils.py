import json
import logging
import os
from typing import Iterator, List

from src.external_api import convert_to_rub

logger = logging.getLogger('transactions')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/transactions.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

current_dir = os.path.dirname(os.path.abspath(__file__))
JSON_DATA = os.path.join(current_dir, '..', 'data', 'operations.json')


def load_transactions(file_path: str) -> list[str]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.exists(file_path):
        logger.error("Файл не найден")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if not isinstance(data, list):
                logger.error("Некорректный формат данных")
                return []
            logger.info("Данные успешно загружены")
            return data
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования JSON")
        return []
    finally:
        logger.info("Завершение функции load_transactions")


transactions = load_transactions(JSON_DATA)
print(transactions)


def gen_transactions(transactions: List[str]) -> Iterator:
    for transaction in transactions:
        yield transaction


transaction_gen = gen_transactions(transactions)


def get_transaction_amount(transaction: dict) -> str:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит конвертация суммы операции в рубли"""
    try:
        amount = transaction.get('operationAmount', {}).get('amount')
        code = transaction.get('operationAmount', {}).get('currency', {}).get('code')
        id = transaction.get('id', {})

        if code == 'RUB':
            return f"Сумма транзакции: {amount} руб. Код валюты: {code}, id: {id}"
        elif code in ["USD", "EUR"]:
            exchange_rate = convert_to_rub(code)
            if exchange_rate is None:
                raise ValueError("Что-то пошло не так, данные с API не подгрузились")
            result = round(float(amount) * exchange_rate, 4)
            return f"Сумма транзакции: {result} руб. Код валюты: {code}, id: {id}"
        else:
            raise ValueError(f"Unsupported currency: {code}")

    except ValueError as e:
        logger.error(f"Ошибка: {e}")
        raise
    finally:
        logger.info("Завершение функции get_transaction_amount")


if __name__ == "__main__":
    try:
        for trans in transaction_gen:
            print(get_transaction_amount(trans))
    except ValueError as e:
        print(e)
