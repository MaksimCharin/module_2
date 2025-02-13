import time

from src.csv_xlsx_reader import read_csv_file, read_xlsx_file
from src.processing import filter_by_state, sort_by_date
from src.re_random import get_dict_by_search_string
from src.search_operations import filter_ruble_transactions, print_transaction
from src.utils import load_transactions


def main() -> None:
    """Основная функция для обработки транзакций."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    file_open = input(
        """Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n
Ответ: """
    )

    if file_open == "1":
        file_path = "../data/operations.json"
        transactions = load_transactions(file_path)
    elif file_open == "2":
        file_path = "../data/transactions.csv"
        transactions = read_csv_file(file_path)
    elif file_open == "3":
        file_path = "../data/transactions_excel.xlsx"
        transactions = read_xlsx_file(file_path)
    else:
        print("Некорректный ввод, повторите ввод")
        return

    while True:
        status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").strip().upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(transactions, status)
            print(f'Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    sort_order = input("Отсортировать операции по дате? (Да/Нет): ").strip().lower()
    if sort_order == "да":
        order = input("По возрастанию или убыванию? (1 - возрастанию, 2 - убыванию): ").strip()
        transactions = sort_by_date(transactions, reverse=(order == "2"))

    ruble_only = input("Выводить только рублевые транзакции? (Да/Нет): ").strip().lower()
    if ruble_only == "да":
        transactions = filter_ruble_transactions(transactions)

    keyword = input("Отфильтровать список транзакций по ключевому слову? (Да/Нет): ").strip().lower()
    if keyword == "да":
        search_string = input("Введите ключевое слово для поиска: ").strip()
        transactions = get_dict_by_search_string(transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    time.sleep(2)
    print_transaction(transactions)


if __name__ == "__main__":
    main()