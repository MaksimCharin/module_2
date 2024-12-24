from masks import get_mask_account, get_mask_card_number


def mask_account_card(input_values: str) -> str:
    """Функция принимает строку, содержащую тип и номер карты или счета."""
    input_values_list = input_values.split()
    input_values_name = input_values_list[0]

    if input_values_name.startswith("Счет"):

        if not input_values_list[-1].isdigit() or len(input_values_list[-1]) < 4:
            return "Вы ввели некорректное значение номера аккаунта"
        else:
            mask_values = get_mask_account(input_values_list[-1])
            input_values_list[-1] = mask_values
            return " ".join(input_values_list)

    elif input_values_name.startswith(("Maestro", "MasterCard", "Visa")):

        if len(input_values_list[-1]) != 16 or not input_values_list[-1].isdigit():
            return "Вы ввели некорректное значение для номера карты"
        else:
            mask_values = get_mask_card_number(input_values_list[-1])
            input_values_list[-1] = mask_values
            return " ".join(input_values_list)

    else:
        return "Вы ввели некорректное название карты/номера счета"


def get_date(date_str: str) -> str:
    """
    Функция принимает строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ".
    """
    date_list = date_str.split('T')
    date_part = date_list[0].split('-')

    dd = date_part[2]
    mm = date_part[1]
    yy = date_part[0]

    return f'{dd}.{mm}.{yy}'


if __name__ == "__main__":
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(get_date('2024-03-11T02:26:18.671407'))
