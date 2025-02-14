import pytest

from src.masks import get_mask_account, get_mask_card


@pytest.mark.parametrize(
    "x, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_get_mask_card(x: str, expected: str) -> None:
    assert get_mask_card(x) == expected


@pytest.mark.parametrize(
    "y, expected",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(y: str, expected: str) -> None:
    assert get_mask_account(y) == expected
