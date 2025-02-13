import unittest
from typing import Any
from unittest.mock import mock_open, patch

import pandas as pd

from src.csv_xlsx_reader import read_csv_file, read_xlsx_file


def test_read_valid_csv():
    """Тест на чтение валидного CSV с использованием моковой заглушки."""
    csv_content = "name;age;city\nAlice;30;New York\nBob;25;Los Angeles"

    expected_output = [
        {"name": "Alice", "age": "30", "city": "New York"},
        {"name": "Bob", "age": "25", "city": "Los Angeles"},
    ]

    with patch("builtins.open", mock_open(read_data=csv_content)):
        result = read_csv_file("dummy_path.csv")
        assert result == expected_output, f"Ожидалось {expected_output}, но получили {result}"


def test_valid_csv_file() -> None:
    """Проверка функции read_csv_file на обработку файла другого формата"""
    file_path = "data.txt"
    file_content = "Это не CSV файл, а просто текстовый файл"
    with patch("builtins.open", mock_open(read_data=file_content)):
        transactions_ = read_csv_file(file_path)
        assert transactions_ == []


@patch("pandas.read_excel")
def test_read_from_xlsx(read_excel: Any) -> None:
    """Тестирование функции read_xlsx_file"""
    read_excel.return_value = pd.DataFrame({"Date": ["2022-01-01", "2022-02-01"], "Amount": [100.00, 200.00]})
    result_read_xlsx_file = read_xlsx_file("../data/transactions_excel.xlsx")
    expected_result = [{"Date": "2022-01-01", "Amount": 100.00}, {"Date": "2022-02-01", "Amount": 200.00}]
    unittest.TestCase().assertEqual(result_read_xlsx_file, expected_result)
