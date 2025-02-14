from datetime import datetime

from src.masks import get_mask_account, get_mask_card


def get_mask_result(string_with_info: str) -> str:
    """Возвращает исходную строку с замаскированным номером карты/счета"""
    division_string = string_with_info.split()
    if division_string[0] == "Счет":
        return f"{' '.join(division_string[:-1])} {get_mask_account(division_string[-1])}"
    return f"{' '.join(division_string[:-1])} {get_mask_card(division_string[-1])}"


def get_date(date_str: str) -> str:
    """Форматирование даты с использованием регулярных выражений."""
    date_formats = [
        "%Y-%m-%dT%H:%M:%S.%f",  # JSON format
        "%Y-%m-%dT%H:%M:%SZ",  # CSV and Excel format
        "%Y-%m-%dT%H:%M:%S",  # General format
    ]

    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(date_str, date_format)
            return date_obj.strftime("%d.%m.%Y")
        except ValueError:
            continue

    return "Некорректный формат даты"
