import pytest

from src.widget import get_date, get_mask_result


@pytest.mark.parametrize(
    "x, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_get_mask_result(x: str, expected: str) -> None:
    """Возвращает исходную строку с замаскированным номером карты/счета"""
    assert get_mask_result(x) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-01-01T00:00:00.000000", "01.01.2024"),
        ("2024-12-31T23:59:59.999999", "31.12.2024"),
        ("2024-02-29T00:00:00.000000", "29.02.2024"),
        ("2023-02-28T00:00:00.000000", "28.02.2023"),
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected
