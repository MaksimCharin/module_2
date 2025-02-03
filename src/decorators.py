from functools import wraps
from typing import Any, Callable, Optional


def log(file_name: Optional[str] = None) -> Callable:
    """Декоратор автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Опционально, при наличии пути файла,
    записывает логи в файл, в противном случае, выводит логи в консоль"""

    def inner(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if file_name:
                    with open(file_name, 'a', encoding='utf-8') as file:
                        file.write(message + '\n')
                else:
                    print(message)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if file_name:
                    with open(file_name, 'a', encoding='utf-8') as file:
                        file.write(message + '\n')
                else:
                    print(message)
                raise e

        return wrapper

    return inner
