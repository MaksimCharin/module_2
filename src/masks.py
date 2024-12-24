from typing import Union


def get_mask_card_number(crd_number: Union[str, int]) -> str:
    """Функция принимает 16-и значный номер карты и возвращает в зашифрованном виде
    в формате: XXXX XX** **** XXXX
    """
    str_crd_number = str(crd_number)

    mask_str = f"{str_crd_number[:6]}******{str_crd_number[-4:]}"
    result_str = f"{mask_str[:4]} {mask_str[4:8]} {mask_str[8:12]} {mask_str[12:]}"

    return result_str


def get_mask_account(acc_number: Union[str, int]) -> str:
    """Функция принимает номер аккаунта и возвращает его зашифрованное представление
    в формате: **XXXX, где XXXX - 4 последние цифры аккаунта
    """
    str_acc_number = str(acc_number)

    return f"**{str_acc_number[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
