import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("1234567890125678") == "1234 56** **** 5678"
    assert get_mask_card_number("4762447890121121") == "4762 44** **** 1121"
    assert get_mask_card_number("6765887890122255") == "6765 88** **** 2255"


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("", "Передана пустая строка"),
        ("1234abcd12345678", "Номер карты должен содержать только цифры"),
        ("123456781234567", "Номер карты должен содержать ровно 16 цифр"),
        ("12345678123456789", "Номер карты должен содержать ровно 16 цифр"),
    ],
)
def test_get_mask_card_number_exceptions(card_number: str, expected: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number(card_number)
    assert str(exc_info.value) == expected


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("73654108430135872701") == "**2701"
    assert get_mask_account("73654108430135875653") == "**5653"


@pytest.mark.parametrize(
    "acc_number, expected",
    [
        ("", "Передана пустая строка"),
        ("73654abc108430135874305", "Номер аккаунта должен содержать только цифры"),
        ("73654108430135", "Номер аккаунта должен содержать ровно 20 цифр"),
        ("73654108430135874305123", "Номер аккаунта должен содержать ровно 20 цифр"),
    ],
)
def test_get_mask_acc_number_exceptions(acc_number: str, expected: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_account(acc_number)
    assert str(exc_info.value) == expected
