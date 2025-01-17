from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_values: str) -> str:
    """Функция принимает строку, содержащую тип и номер карты или счета.
    Возвращает зашифрованное значение"""

    input_values_list = input_values.split()
    input_values_name = input_values_list[0]

    if input_values_name.startswith("Счет"):

        if not input_values_list[-1].isdigit() or len(input_values_list[-1]) != 20:
            raise ValueError("Вы ввели некорректное значение номера аккаунта")
        else:
            mask_values = get_mask_account(input_values_list[-1])
            input_values_list[-1] = mask_values
            return " ".join(input_values_list)

    elif input_values_name.startswith(("Maestro", "MasterCard", "Visa")):

        if len(input_values_list[-1]) != 16 or not input_values_list[-1].isdigit():
            raise ValueError("Вы ввели некорректное значение для номера карты")
        else:
            mask_values = get_mask_card_number(input_values_list[-1])
            input_values_list[-1] = mask_values
            return " ".join(input_values_list)

    else:
        raise ValueError("Вы ввели некорректное название карты/номера счета")


def get_date(date_str: str) -> str:
    """
    Функция принимает строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ".
    """

    if "T" not in date_str or len(date_str) < 26:
        raise ValueError("Некорректный формат даты")

    date_list = date_str.split("T")
    date_part = date_list[0].split("-")

    if len(date_part) != 3:
        raise ValueError("Некорректный формат даты")

    dd = date_part[2]
    mm = date_part[1]
    yy = date_part[0]

    return f"{dd}.{mm}.{yy}"
