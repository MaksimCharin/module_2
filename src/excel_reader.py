import os

import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
EXCEL_DATA = os.path.join(current_dir, '..', 'data', 'transactions_excel.xlsx')

def get_excel_data(data: str) -> list[dict]:
    """Функция принимает на вход файл с данными в xlsx формате, возвращает список словарей с данными"""
    reviews = pd.read_excel(data)
    transactions = reviews.to_dict(orient='records')
    return transactions





if __name__ == '__main__':
    excel_transactions = get_excel_data(EXCEL_DATA)
    print(excel_transactions[:5])
    # for transaction in excel_transactions[:5]:
    #     print(transaction)