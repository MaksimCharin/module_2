import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('acc_card_values, expected',
                         [
                             ("Счет 73654108430135874305", "Счет **4305"),
                             ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                             ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                             ("Visa 2107300734726757", "Visa 2107 30** **** 6757")
                         ])
def test_mask_account_card(acc_card_values, expected):
    assert mask_account_card(acc_card_values) == expected


@pytest.mark.parametrize('acc_card_values, mask_values',
                         [
                             ("Счет 736541084301as135874305", "Вы ввели некорректное значение номера аккаунта"),
                             ("Счет 7365410843011358", "Вы ввели некорректное значение номера аккаунта"),
                             ("Счет 736541084301as135874", "Вы ввели некорректное значение номера аккаунта"),
                             ("Maestro 15968378sa68705199", "Вы ввели некорректное значение для номера карты"),
                             ("Maestro 1596837865199", "Вы ввели некорректное значение для номера карты"),
                             ("Maestro 159asd6837865199", "Вы ввели некорректное значение для номера карты"),
                             ("Счёт 73654108430135874305", "Вы ввели некорректное название карты/номера счета"),
                             ("Maetro 1596837868705199", "Вы ввели некорректное название карты/номера счета"),
                             ("MasteCard 1596837868705199", "Вы ввели некорректное название карты/номера счета")
                         ])
def test_mask_account_card_exceptions(acc_card_values, mask_values):
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(acc_card_values)
    assert str(exc_info.value) == mask_values


@pytest.mark.parametrize('date_str, expected',
                         [
                             ("2024-03-11T02:26:18.671407", "11.03.2024"),
                             ("2024-01-01T00:00:00.000000", "01.01.2024"),
                             ("2024-12-31T23:59:59.999999", "31.12.2024"),
                             ("2024-02-29T00:00:00.000000", "29.02.2024"),
                             ("2023-02-28T00:00:00.000000", "28.02.2023"),
                         ])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected


@pytest.mark.parametrize('date_str, expected',
                         [
                             ("", "Некорректный формат даты"),
                             ("2024-03-11", "Некорректный формат даты"),
                             ("2024-03-11T", "Некорректный формат даты"),
                             ("2024-03-11 02:26:18.671407", "Некорректный формат даты"),
                             ("2024/03/11T02:26:18.671407", "Некорректный формат даты"),
                             ("11.03.2024T02:26:18.671407", "Некорректный формат даты"),
                             ("T02:26:18.671407", "Некорректный формат даты")
                         ])
def test_get_date_invalid(date_str, expected):
    with pytest.raises(ValueError) as exc_info:
        get_date(date_str)
    assert str(exc_info.value) == expected
