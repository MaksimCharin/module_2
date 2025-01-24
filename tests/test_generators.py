import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions: list) -> None:
    expectation = [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }]
    transaction = filter_by_currency(transactions, "USD")
    assert list(*transaction) == expectation


@pytest.mark.parametrize("transactions, currency, expected", [
    ([], "USD", []),
    ([{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }], "USD", [])
])
def test_filter_by_currency_no_exceptions(transactions: list, currency: str, expected: str) -> None:
    result = filter_by_currency(transactions, currency)
    assert list(*result) == expected


@pytest.mark.parametrize("transactions, expected_descriptions", [
    ([{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
         {
             "id": 142264268,
             "state": "EXECUTED",
             "date": "2019-04-04T23:20:05.206878",
             "operationAmount": {
                 "amount": "79114.93",
                 "currency": {
                     "name": "EUR",
                     "code": "EUR"
                 }
             },
             "description": "Перевод со счета на счет",
             "from": "Счет 19708645243227258542",
             "to": "Счет 75651667383060284188"
         }], ["Перевод организации", "Перевод со счета на счет"]),
    ([{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }], ["Перевод организации"]),
    ([], [])
])
def test_transaction_descriptions(transactions: list, expected_descriptions: str) -> None:
    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions


@pytest.mark.parametrize("start, end, expected", [
    (0, 0, ["0000 0000 0000 0000"]),
    (1, 1, ["0000 0000 0000 0001"]),
    (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
    (1234567890123456, 1234567890123458, ["1234 5678 9012 3456", "1234 5678 9012 3457", "1234 5678 9012 3458"])
])
def test_card_number_generator(start: int, end: int, expected: int) -> None:
    result = list(card_number_generator(start, end))
    assert result == expected


def test_card_number_generator_empty_range() -> None:
    start = 10
    end = 9
    result = list(card_number_generator(start, end))
    assert result == []


def test_card_number_generator_large_range() -> None:
    start = 0
    end = 1000
    result = list(card_number_generator(start, end))
    assert len(result) == 1001
    assert result[0] == "0000 0000 0000 0000"
    assert result[-1] == "0000 0000 0000 1000"
