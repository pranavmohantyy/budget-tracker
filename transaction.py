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


def monthly_summary():
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expenses = sum(t.amount for t in transactions if t.type == 'expense')
    net_balance = total_income - total_expenses
    return {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_balance': net_balance
    }