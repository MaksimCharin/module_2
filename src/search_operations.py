from typing import Any, Dict, List

from src.csv_xlsx_reader import read_csv_file, read_xlsx_file
from src.generators import transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.re_random import get_dict_by_search_string
from src.utils import load_transactions
from src.widget import get_date, get_mask_result


def format_open_file() -> Any:
    """Функция для открытия определённого файла"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    file_open = input(
        """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n
Ответ: """
    )
    if file_open == "1" or file_open.lower() == "json":
        print("Для обработки выбран JSON файл.")
        return load_transactions("data/operations.json")
    elif file_open == "2" or file_open.lower() == "csv":
        print("Для обработки выбран CSV файл.")
        return read_csv_file("../data/transactions.csv")
    elif file_open == "3" or file_open.lower() == "excel":
        print("Для обработки выбран Excel файл.")
        return read_xlsx_file("data/transactions_excel.xlsx")
    else:
        print("Некорректный ввод, повторите ввод")
        return format_open_file()


def filter_status(data: list) -> list:
    """Функция для выбора статуса EXECUTED, CANCELED, PENDING"""
    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    format_ = input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
    if format_.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
        print("Статус не корректен, введите ещё раз")
        return filter_status(data)

    data = filter_by_state(data, format_.upper())
    return data


def sort_transaction_by_date(data: list) -> list | dict:
    """Сортирует список транзакций"""
    sort = input("Отсортировать операции по дате? Да/Нет \n")
    if sort.lower() == "да":
        figure = input("1.По возрастанию 2.По убыванию \n")
        if figure.lower() in ["по возрастанию", "1"]:
            return sort_by_date(data)
        elif figure.lower() in ["по убыванию", "2"]:
            return sort_by_date(data, reverse=False)
        else:
            print("Не корректное значение, введите ещё раз")
            return sort_transaction_by_date(data)
    elif sort.lower() == "нет":
        return data
    else:
        print("Не корректный ответ, повторите ввод")
        return sort_transaction_by_date(data)


def filter_ruble_transactions(operations: List[Dict]) -> List[Dict]:
    """Фильтрация транзакций только с рублевой валютой."""
    return [op for op in operations if op.get("operationAmount", {}).get("currency", {}).get("name") == "руб."]


def filter_user_keyword(data: list) -> Any:
    """Фильтрация по введённому слову"""
    keyword = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n")
    if keyword.lower() == "да":
        find_ = input("Что бы вы хотели найти?\n")
        return get_dict_by_search_string(data, find_)
    elif keyword.lower() == "нет":
        return data
    else:
        print("Некорректный ввод, введите ещё раз")
        return filter_user_keyword(data)


def print_transaction(data: List[Dict]) -> None:
    """Вывод транзакций."""
    if not data:
        print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")
        return

    descriptions = transaction_descriptions(data)
    for transaction, desc in zip(data, descriptions):
        print(get_date(transaction["date"]), desc)
        if "Перевод" in transaction["description"]:
            print(
                get_mask_result(transaction.get("from", "Неизвестно")),
                "->",
                get_mask_result(transaction.get("to", "Неизвестно")),
            )
        else:
            print(get_mask_result(transaction.get("to", "Неизвестно")))
            amount = transaction.get("operationAmount", {}).get("amount", transaction.get("amount", "Неизвестно"))
            currency = (
                transaction.get("operationAmount", {})
                .get("currency", {})
                .get("name", transaction.get("currency_name", "Неизвестно"))
            )
            print(f"Сумма: {amount} {currency}")
