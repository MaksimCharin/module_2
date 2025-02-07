import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sorted_values):
    expected_executed = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]
    expected_canceled = [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
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


@pytest.mark.parametrize(
    "operations, reverse, expected",
    [
        (
                [
                    {"id": 1, "state": "EXECUTED", "date": "2024-01-01"},
                    {"id": 2, "state": "EXECUTED", "date": "2023-01-01"},
                    {"id": 3, "state": "CANCELED", "date": "2022-01-01"},
                ],
                True,
                "Некорректный формат даты",
        ),
        (
                [
                    {"id": 1, "state": "EXECUTED", "date": "2024-01-01"},
                    {"id": 2, "state": "EXECUTED", "date": "2023-01-01"},
                    {"id": 3, "state": "CANCELED", "date": "2022-01-01"},
                ],
                False,
                "Некорректный формат даты",
        ),
        (
                [
                    {"id": 1, "date": ""},
                    {"id": 2, "date": "2024-01-01"},
                    {"id": 3, "date": "2024-01-01"},
                ],
                True,
                "Некорректный формат даты",
        ),
        (
                [
                    {"id": 1, "date": "Incorrect Value"},
                    {"id": 2, "date": "2024-01-01"},
                    {"id": 3, "date": "2024-01-01"},
                ],
                False,
                "Некорректный формат даты",
        ),
    ],
)
def test_sort_by_date_exceptions(operations: list, reverse: bool, expected: str) -> None:
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(operations, reverse)

    assert str(exc_info.value) == expected
