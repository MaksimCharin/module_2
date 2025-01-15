import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sort_by_state_value: tuple) -> None:
    for each_test_value in sort_by_state_value:
        operations, key_value, expected = each_test_value
        assert filter_by_state(operations, key_value) == expected


def test_sort_by_date(sort_by_date_value: tuple) -> None:
    for each_test_value in sort_by_date_value:
        operations, key_value, expected = each_test_value
        assert sort_by_date(operations, key_value) == expected


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
