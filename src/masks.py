import logging
from typing import Union

logger = logging.getLogger('mask_card_number')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/mask_card_account.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(crd_number: Union[str, int]) -> str:
    """Функция принимает 16-и значный номер карты и возвращает в зашифрованном виде
    в формате: XXXX XX** **** XXXX
    """
    str_crd_number = str(crd_number)

    try:
        if not str_crd_number:
            raise ValueError("Передана пустая строка")
        if len(str_crd_number) != 16:
            raise ValueError("Номер карты должен содержать ровно 16 цифр")
        if not str_crd_number.isdigit():
            raise ValueError("Номер карты должен содержать только цифры")

        mask_str = f"{str_crd_number[:6]}******{str_crd_number[-4:]}"
        result_str = f"{mask_str[:4]} {mask_str[4:8]} {mask_str[8:12]} {mask_str[12:]}"

        logger.info(f"Номер карты успешно замаскирован: {result_str}")
        return result_str

    except ValueError as e:
        logger.error(f"Ошибка: {e}")
        raise

    finally:
        logger.info("Завершение функции get_mask_card_number")


def get_mask_account(acc_number: Union[str, int]) -> str:
    """Функция принимает номер аккаунта и возвращает его зашифрованное представление
    в формате: **XXXX, где XXXX - 4 последние цифры аккаунта
    """
    str_acc_number = str(acc_number)

    try:
        if not str_acc_number:
            raise ValueError("Передана пустая строка")
        if not str_acc_number.isdigit():
            raise ValueError("Номер аккаунта должен содержать только цифры")
        if len(str_acc_number) != 20:
            raise ValueError("Номер аккаунта должен содержать ровно 20 цифр")

        masked_account = f"**{str_acc_number[-4:]}"

        logger.info(f"Номер аккаунта успешно замаскирован: {masked_account}")
        return masked_account

    except ValueError as e:
        logger.error(f"Ошибка: {e}")
        raise

    finally:
        logger.info("Завершение функции get_mask_account")

    return masked_account


if __name__ == "__main__":
    try:
        print(get_mask_card_number("1234567890123456"))  # Успешный случай
        print(get_mask_account("12345678901234567890"))  # Успешный случай
    except ValueError as e:
        print(e)
