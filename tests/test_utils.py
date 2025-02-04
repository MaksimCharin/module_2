import json
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

from src.utils import get_transaction_amount, load_transactions


def test_load_transactions_file_found() -> None:
    test_data: List[Dict[str, Any]] = [{"id": 1, "amount": 100}]
    with patch("os.path.exists", return_value=True), patch(
        "builtins.open", mock_open(read_data=json.dumps(test_data))
    ):
        result: List[Dict[str, Any]] = load_transactions("existing_file.json")
        assert result == test_data


def test_load_transactions_file_not_found() -> None:
    with patch("os.path.exists", return_value=False):
        result: List[Dict[str, Any]] = load_transactions("non_existent_file.json")
        assert result == []


def test_load_transactions_invalid_json() -> None:
    with patch("os.path.exists", return_value=True), patch(
        "builtins.open", mock_open(read_data='{"id": 1, "amount": 100}')
    ):
        result: List[Dict[str, Any]] = load_transactions("invalid_json_file.json")
        assert result == []


def test_get_transaction_amount_rub() -> None:
    transaction: Dict[str, Any] = {"id": 1, "operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}}
    result: str = get_transaction_amount(transaction)
    assert result == "Сумма транзакции: 100.0 руб. Код валюты: RUB, id: 1"


def test_get_transaction_amount_usd() -> None:
    transaction: Dict[str, Any] = {"id": 1, "operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}
    with patch("src.utils.convert_to_rub", return_value=75.0):
        result: str = get_transaction_amount(transaction)
        assert result == "Сумма транзакции: 7500.0 руб. Код валюты: USD, id: 1"
