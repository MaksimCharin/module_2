from typing import Dict, List

from src.widget import get_date


def filter_by_state(operations: List[dict], key_value: str = "EXECUTED") -> List[dict]:
    """Функция возвращает список словарей, у которых ключ state соответствует указанному значению"""
    filtered_operations = []
    for operation in operations:
        if operation.get("state") == key_value:
            filtered_operations.append(operation)

    return filtered_operations


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортировка транзакций по дате."""
    valid_operations = []
    for operation in operations:
        date_str = operation.get("date")
        if get_date(date_str) != "Некорректный формат даты":
            valid_operations.append(operation)

    return sorted(valid_operations, key=lambda x: x["date"], reverse=reverse)
