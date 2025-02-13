import csv
import os
from typing import Any

import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
CSV_DATA = os.path.join(current_dir, "..", "data", "transactions.csv")
XLSX_DATA = os.path.join(current_dir, "..", "data", "transactions_excel.xlsx")


def read_csv_file(filename: str) -> list:
    data = []
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            data.append(row)
    return data


def read_xlsx_file(filename: str) -> list[Any]:
    if filename.endswith(".xlsx"):
        data = pd.read_excel(filename)
        return data.to_dict("records")
    else:
        return []
