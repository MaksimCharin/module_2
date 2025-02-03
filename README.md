# Виджет банковских операций клиента

## Описание:

Разработка функционала банковского приложения в ЛК клиента. На данный момент включает в себя маскировку карты/аккаунта,
сортировку информации по дате или искомому значению, перевод и показ даты в удобном формате.

## Установка:

1. Клонируйте репозиторий:

```
git clone https://github.com/MaksimCharin/module_2.git
```

2. Установите зависимости:

```
pip install -r requirements.txt
```

## Использование:

1. В директории SRC, в модуле: *masks.py* можно посмотреть изнутри работу функций по маскировке данных,
выполнив внутри модуля код ниже:
```
if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
```
2. В директории SRC, в модуле: *widget.py* можно протестировать работу новой функции по маскировке данных + работу
   функции по работе с датой. Для демонстрации, внутри модуля можно выполнить код, представленный ниже
   (вводимые данные могут быть произвольными):
```
if __name__ == "__main__":
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(get_date("2024-03-11T02:26:18.671407"))

```
3. В директории SRC, в модуле: *processing.py* можно посмотреть работу функций по сортировке данных. Внтури модуля
представлены значения для демонстрации работы функций (данные можно менять)


4. В директории SRC, в модуле: *generators.py* реализованы функция-генератор для банковских карт, а так же 2 функции
для работы с транзакциями *filter_by_currency* - позволяет поочередно отображать транзакции по заданной валюте
и функция *transaction_descriptions* - позволяет получить краткое описание операции (примеры работы данных функций
и тестовые значения реализованы в модуле test_generators)


5. В директории SRC, в модуле: *decorators.py* реалищзован декоратор *log* позволяющий записывать логи функций в файл
или выводить информацию в консоль, в зависимости от того, было передано file_name (место для сохранения логов) или нет
## Тестирование
Перед запуском тестов убедитесь, что у вас установлены все необходимые зависимости. 
Вы можете установить их с помощью следующей команды:

```
pip install -r requirements.txt
```

## Запуск тестов
Для запуска тестов используйте команду:
```
pytest
```
## Пример работы теста
С помощью декоратора реализована параметризация тестов (запуск одного и того же теста с различными входными данными)
```
@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-01-01T00:00:00.000000", "01.01.2024"),
        ("2024-12-31T23:59:59.999999", "31.12.2024"),
        ("2024-02-29T00:00:00.000000", "29.02.2024"),
        ("2023-02-28T00:00:00.000000", "28.02.2023"),
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    assert get_date(date_str) == expected
```
```
@pytest.mark.parametrize("start, end, expected", [
    (0, 0, ["0000 0000 0000 0000"]),
    (1, 1, ["0000 0000 0000 0001"]),
    (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),
    (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"]),
    (1234567890123456, 1234567890123458, ["1234 5678 9012 3456", "1234 5678 9012 3457", "1234 5678 9012 3458"])
])
def test_card_number_generator(start: int, end: int, expected: int) -> None:
    result = list(card_number_generator(start, end))
    assert result == expected


def test_card_number_generator_empty_range() -> None:
    start = 10
    end = 9
    result = list(card_number_generator(start, end))
    assert result == []


def test_card_number_generator_large_range() -> None:
    start = 0
    end = 1000
    result = list(card_number_generator(start, end))
    assert len(result) == 1001
    assert result[0] == "0000 0000 0000 0000"
    assert result[-1] == "0000 0000 0000 1000"
```
Пример работы декоратора *log* с переданным file_name (ожидаем вывод ошибки в файл. для корректности разовой проверки
необходимо закомментировать последнюю строчку и удалить файл вручную перед след. тестом)
```
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
```
Пример работы декоратора *log* без переданного file_name (ожидаем вывод ошибки в консоль)
```
@log()
    def summ(a: int, b: int) -> int:
        return a + b

    with pytest.raises(TypeError):
        summ(2, '5')

    captured = capsys.readouterr()
    assert captured.out == "summ error: TypeError. Inputs: (2, '5'), {}\n"
```
В проекте представлена реализация юнит-тестов, которые проверяют отдельные функции и методы. 
Находятся в директории [tests/](https://github.com/MaksimCharin/module_2/tree/feature/homework_11_1/tests)
## Покрытие кода тестами
Для проверки покрытия кода тестами используйте команду:
```
pytest --cov=my_module tests/
```
или можно перейти по [ссылке](https://github.com/MaksimCharin/module_2/tree/feature/homework_11_1/htmlcov/index.html)


## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).