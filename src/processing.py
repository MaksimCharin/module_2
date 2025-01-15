from typing import List, Optional


def filter_by_state(operations: List[dict], key_value: str = "EXECUTED") -> List[dict]:
    """Функция возвращает список словарей, у которых ключ state соответствует указанному значению"""
    filtered_operations = []
    for operation in operations:
        if operation.get("state") == key_value:
            filtered_operations.append(operation)

    return filtered_operations


def sort_by_date(operations: List[dict], reverse: Optional[bool] = True) -> List[dict]:
    """Функция сортирует список словарей по дате (значение по умолчанию - по убыванию)"""
    if reverse is None:
        reverse = True

    for operation in operations:
        tuple_from_values = tuple(operation.values())
        if "T" not in tuple_from_values[-1] or len(tuple_from_values[-1]) < 26:
            raise ValueError("Некорректный формат даты")

    sorted_operations = sorted(operations, key=lambda each_dict: each_dict["date"], reverse=reverse)

    return sorted_operations
