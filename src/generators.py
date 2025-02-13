from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """Функция возвращает итератор, который поочередно выдает транзакции по заданной валюте"""
    yield (
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["name"] == currency
    )


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Возвращает итератор по описаниям транзакций"""
    for item in transactions:
        yield item["description"]


def card_number_generator(start: int = 0, end: int = 9999999999999999) -> Iterator[str]:
    """Функция-генератор, которая выдает номера банковских карт в формате:
    XXXX XXXX XXXX XXXX, где X — цифра номера
    """

    for i in range(start, end + 1):
        card_number = f"{i:016}"
        formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield formatted_card_number