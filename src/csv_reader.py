import csv
import os
from typing import Dict, List

current_dir = os.path.dirname(os.path.abspath(__file__))
CSV_DATA = os.path.join(current_dir, '..', 'data', 'transactions.csv')

def get_csv_data(data: str) -> List[Dict[str, str]]:
    """Функция принимает на вход файл с данными в csv формате, возвращает список словарей с данными"""
    try:
        with open(data, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            result = list(reader)
            return result
    except FileNotFoundError:
        raise
    except Exception:
        raise

if __name__ == '__main__':
    try:
        transactions = get_csv_data(CSV_DATA)
        print(transactions[:5])
    except Exception:
        raise