import re
from collections import Counter
from typing import Dict, List


def get_dict_by_search_string(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Фильтрация транзакций по ключевому слову."""
    return [t for t in transactions if re.search(search_string, t.get("description", ""), re.IGNORECASE)]


def categorize_transactions(transactions_list: list, categories: dict) -> dict:
    """Подсчет операций в каждой категории"""
    category_counts_2: dict = Counter()

    for transaction in transactions_list:
        if "description" in transaction:
            for category, keywords in categories.items():
                if any(keyword.lower() in transaction["description"].lower() for keyword in keywords):
                    category_counts_2[category] += 1
                    break

    return dict(category_counts_2)
