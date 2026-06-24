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


def load_transactions():
    global transactions
    try:
        with open('budget_data.json', 'r') as f:
            data = json.load(f)
            transactions = [Transaction(**item) for item in data]
    except FileNotFoundError:
        transactions = []


def category_breakdown():
    total_expenses = sum(t.amount for t in transactions if t.type == 'expense')
    category_totals = {}
    for t in transactions:
        if t.type == 'expense':
            category_totals[t.category] = category_totals.get(t.category, 0) + t.amount
    breakdown = {category: {'amount': amount, 'percentage': (amount / total_expenses * 100 if total_expenses > 0 else 0)} for category, amount in category_totals.items()}
    return breakdown
