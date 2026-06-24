from dataclasses import dataclass
from datetime import datetime
import json

@dataclass
class Transaction:
    date: datetime
    amount: float
    category: str
    description: str
    type: str  # 'income' or 'expense'

    def __post_init__(self):
        if self.type not in ['income', 'expense']:
            raise ValueError('type must be either income or expense')

transactions = []

budgets = {}


def load_transactions():
    global transactions
    try:
        with open('budget_data.json', 'r') as f:
            data = json.load(f)
            transactions = [Transaction(**item) for item in data]
    except FileNotFoundError:
        transactions = []


def filter_transactions_by_date(year_month):
    year, month = year_month.split('-')
    filtered = [t for t in transactions if t.date.strftime('%Y-%m') == f'{year}-{month}']
    return filtered
