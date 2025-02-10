from unittest.mock import patch

import pandas as pd

from src.excel_reader import get_excel_data


def test_read_valid_excel() -> None:
    expected_result = [
        {
            'id': 650703,
            'state': 'EXECUTED',
            'date': '2023-09-05T11:30:32Z',
            'amount': 16210,
            'currency_name': 'Sol',
            'currency_code': 'PEN',
            'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397',
            'description': 'Перевод организации'
        },
        {
            'id': 650704,
            'state': 'EXECUTED',
            'date': '2023-09-06T12:30:32Z',
            'amount': 20000,
            'currency_name': 'Dollar',
            'currency_code': 'USD',
            'from': 'Счет 12345678901234567890',
            'to': 'Счет 98765432109876543210',
            'description': 'Перевод сотруднику'
        }
    ]

    mock_df = pd.DataFrame(expected_result)

    with patch('pandas.read_excel', return_value=mock_df):
        result = get_excel_data('fake_path.xlsx')
        assert result == expected_result

def test_file_not_found() -> None:
    with patch('pandas.read_excel', side_effect=FileNotFoundError):
        try:
            get_excel_data('nonexistent.xlsx')
            assert False
        except FileNotFoundError:
            assert True

def test_invalid_excel_format() -> None:
    invalid_df = pd.DataFrame({'invalid_column': ['invalid data']})

    with patch('pandas.read_excel', return_value=invalid_df):
        try:
            get_excel_data('invalid.xlsx')
            assert False
        except Exception:
            assert True

if __name__ == '__main__':
    test_read_valid_excel()
    test_file_not_found()
    test_invalid_excel_format()
    print("All tests passed!")