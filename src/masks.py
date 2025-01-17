from typing import Union


def get_mask_card_number(crd_number: Union[str, int]) -> str:
    """Функция принимает 16-и значный номер карты и возвращает в зашифрованном виде
    в формате: XXXX XX** **** XXXX
    """
    str_crd_number = str(crd_number)

    if not str_crd_number:
        raise ValueError("Передана пустая строка")
    if len(str_crd_number) != 16:
        raise ValueError("Номер карты должен содержать ровно 16 цифр")
    if not str_crd_number.isdigit():
        raise ValueError("Номер карты должен содержать только цифры")

    mask_str = f"{str_crd_number[:6]}******{str_crd_number[-4:]}"
    result_str = f"{mask_str[:4]} {mask_str[4:8]} {mask_str[8:12]} {mask_str[12:]}"

    return result_str


def get_mask_account(acc_number: Union[str, int]) -> str:
    """Функция принимает номер аккаунта и возвращает его зашифрованное представление
    в формате: **XXXX, где XXXX - 4 последние цифры аккаунта
    """
    str_acc_number = str(acc_number)

    if not str_acc_number:
        raise ValueError("Передана пустая строка")
    if not str_acc_number.isdigit():
        raise ValueError("Номер аккаунта должен содержать только цифры")
    if len(str_acc_number) != 20:
        raise ValueError("Номер аккаунта должен содержать ровно 20 цифр")

    return f"**{str_acc_number[-4:]}"
