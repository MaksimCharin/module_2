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


if __name__ == "__main__":
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
