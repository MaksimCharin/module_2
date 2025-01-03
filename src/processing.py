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
    sorted_operations = sorted(operations, key=lambda each_dict: each_dict["date"], reverse=reverse)

    return sorted_operations


if __name__ == "__main__":
    result = filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        "CANCELED",
    )

    print(result)
    lst_ = [
        {"id": 1, "state": "EXECUTED", "date": "2020-06-30T02:08:58.425572"},
        {"id": 2, "state": "CANCELED", "date": "2017-09-12T21:27:25.241689"},
        {"id": 3, "state": "CANCELED", "date": "2021-10-14T08:21:33.419441"},
        {"id": 4, "state": "EXECUTED", "date": "2023-07-03T18:35:29.512364"},
        {"id": 5, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 6, "state": "CANCELED", "date": "2024-05-02T18:35:29.512364"},
    ]

    print(sort_by_date(lst_))
