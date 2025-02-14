import logging

logger = logging.getLogger("mask_card_number")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s",
    filename="../logs/mask_card_account.log",
    encoding="utf-8",
    filemode="w",
)


def get_mask_card(number_card: str) -> str:
    """Функции, возвращающая маску карты"""
    if len(number_card) == 16:
        number_card = str(number_card).replace(" ", "")
        logger.info("Функция get_mask_card выполнена успешно")
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"
    else:
        logger.error("В функции get_mask_card что-то пошло не так")
        return ""


def get_mask_account(number_card: str) -> str:
    """Функции, возвращающая маску счета"""
    if len(number_card) == 20:
        number_card = str(number_card).replace(" ", "")
        logger.info("Функция get_mask_account выполнена успешно")
        return f"**{number_card[-4:]}"
    else:
        logger.error("В функции get_mask_account что-то пошло не так")
        return ""


if __name__ == "__main__":
    try:
        print(get_mask_card("1234567890123456"))  # Успешный случай
        print(get_mask_account("12345678901234567890"))  # Успешный случай
    except ValueError as e:
        print(e)
