import time

from src.processing import filter_by_state, sort_by_date
from src.re_random import get_dict_by_search_string
from src.search_operations import filter_ruble_transactions, print_transaction, format_open_file


def main() -> None:
    """Основная функция для обработки транзакций."""
    transactions_list = format_open_file()

    while True:
        status = input("Введите статус для фильтрации (EXECUTED, CANCELED, PENDING): ").strip().upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(transactions_list, status)
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
