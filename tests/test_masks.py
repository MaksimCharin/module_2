import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(valid_card_number_list: list) -> None:
    for crd_number, mask_value in valid_card_number_list:
        assert get_mask_card_number(crd_number) == mask_value


def test_get_mask_card_number_exceptions(invalid_card_number_list: list) -> None:
    for crd_number, exception_message in invalid_card_number_list:
        with pytest.raises(ValueError) as exc_info:
            get_mask_card_number(crd_number)

        assert str(exc_info.value) == exception_message


def test_get_mask_account(valid_acc_number_list: list) -> None:
    for acc_number, mask_value in valid_acc_number_list:
        assert get_mask_account(acc_number) == mask_value


def test_get_mask_acc_number_exceptions(invalid_acc_number_list: list) -> None:
    for acc_number, exception_message in invalid_acc_number_list:
        with pytest.raises(ValueError) as exc_info:
            get_mask_account(acc_number)

        assert str(exc_info.value) == exception_message
