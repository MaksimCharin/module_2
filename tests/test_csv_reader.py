from unittest.mock import mock_open, patch

from src.csv_reader import get_csv_data


def test_read_valid_csv() -> None:
    expected_result = [
        {
            'id': '650703',
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': '16210',
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        },
        {
            'id': '650704',
            'state': 'EXECUTED',
            'date': '2023-09-06T12:30:32Z',
            'amount': '20000',
            'currency_name': 'Dollar',
            'currency_code': 'USD',
            'from': 'Счет 12345678901234567890',
            'to': 'Счет 98765432109876543210',
            'description': 'Перевод сотруднику'
        }
    ]

    csv_content = (
        "id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n"
        "650704;EXECUTED;2023-09-06T12:30:32Z;20000;Dollar;USD;Счет 12345678901234567890;Счет 98765432109876543210;Перевод сотруднику\n"
    )

    with patch('builtins.open', mock_open(read_data=csv_content)):
        result = get_csv_data('fake_path.csv')
        assert result == expected_result

def test_file_not_found() -> None:
    with patch('builtins.open', side_effect=FileNotFoundError):
        try:
            get_csv_data('nonexistent.csv')
            assert False, "Expected FileNotFoundError"
        except FileNotFoundError:
            assert True

def test_invalid_csv_format() -> None:
    invalid_csv_content = "invalid data"

    with patch('builtins.open', mock_open(read_data=invalid_csv_content)):
        try:
            get_csv_data('invalid.csv')
            assert False, "Expected Exception"
        except Exception:
            assert True