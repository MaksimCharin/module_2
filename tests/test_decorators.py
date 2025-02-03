import os
from typing import Any

import pytest

from src.decorators import log


def test_console_log_success(capsys: Any) -> None:
    @log()
    def summ(a: int, b: int) -> int:
        return a + b

    summ(2, 3)

    captured = capsys.readouterr()
    assert captured.out == "summ ok\n"


def test_console_log_error(capsys: Any) -> None:
    @log()
    def summ(a: int, b: int) -> int:
        return a + b

    with pytest.raises(TypeError):
        summ(2, '5')

    captured = capsys.readouterr()
    assert captured.out == "summ error: TypeError. Inputs: (2, '5'), {}\n"


def test_writing_log_success() -> None:
    log_file = "mylog.txt"

    @log(log_file)
    def summ(a: int, b: int) -> int:
        return a + b

    summ(2, 3)

    with open(log_file, 'r', encoding='utf-8') as file:
        log_content = file.read()

    expected_log = "summ ok\n"
    assert log_content == expected_log

    # удаляет файл с содержимым, после пройденного тест
    os.remove(log_file)


def test_writing_log_error() -> None:
    log_file = "mylog.txt"

    @log(log_file)
    def summ(a: int, b: int) -> int:
        return a + b

    with pytest.raises(TypeError):
        summ(2, "5")  # type: ignore

    with open(log_file, 'r', encoding='utf-8') as file:
        log_content = file.read()

    expected_log = "summ error: TypeError. Inputs: (2, '5'), {}\n"
    assert log_content == expected_log

    # удаляет файл с содержимым, после пройденного тест
    os.remove(log_file)
