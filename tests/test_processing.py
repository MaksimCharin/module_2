from typing import Dict, List

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sorted_values):
    expected_executed = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    expected_canceled = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    key = "CANCELED"
    assert filter_by_state(sorted_values, key) == expected_canceled
    assert filter_by_state(sorted_values) == expected_executed


def test_sort_by_date(sorted_values):
    expected_false = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

    expected_true = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    reverse = False
    assert sort_by_date(sorted_values) == expected_true
    assert sort_by_date(sorted_values, reverse) == expected_false


def test_sort_by_date_reverse_true() -> None:
    """Проверка сортировки по дате в порядке убывания."""
    operations: List[Dict] = [
        {"date": "2023-10-01T12:00:00", "amount": 100},
        {"date": "2023-10-03T12:00:00", "amount": 200},
        {"date": "2023-10-02T12:00:00", "amount": 150},
    ]

    sorted_operations = sort_by_date(operations, reverse=True)

    # Ожидаемый результат: транзакции отсортированы по дате в порядке убывания
    expected_result = [
        {"date": "2023-10-03T12:00:00", "amount": 200},
        {"date": "2023-10-02T12:00:00", "amount": 150},
        {"date": "2023-10-01T12:00:00", "amount": 100},
    ]

    assert sorted_operations == expected_result


def test_sort_by_date_reverse_false() -> None:
    """Проверка сортировки по дате в порядке возрастания."""
    operations: List[Dict] = [
        {"date": "2023-10-01T12:00:00", "amount": 100},
        {"date": "2023-10-03T12:00:00", "amount": 200},
        {"date": "2023-10-02T12:00:00", "amount": 150},
    ]

    sorted_operations = sort_by_date(operations, reverse=False)

    # Ожидаемый результат: транзакции отсортированы по дате в порядке возрастания
    expected_result = [
        {"date": "2023-10-01T12:00:00", "amount": 100},
        {"date": "2023-10-02T12:00:00", "amount": 150},
        {"date": "2023-10-03T12:00:00", "amount": 200},
    ]

    assert sorted_operations == expected_result


def test_sort_by_date_invalid_dates() -> None:
    """Проверка обработки транзакций с некорректными датами."""
    operations: List[Dict] = [
        {"date": "2023-10-01T12:00:00", "amount": 100},
        {"date": "некорректная дата", "amount": 200},  # Некорректная дата
        {"date": "2023-10-02T12:00:00", "amount": 150},
    ]

    sorted_operations = sort_by_date(operations, reverse=True)

    # Ожидаемый результат: транзакция с некорректной датой исключена
    expected_result = [
        {"date": "2023-10-02T12:00:00", "amount": 150},
        {"date": "2023-10-01T12:00:00", "amount": 100},
    ]

    assert sorted_operations == expected_result
