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


def load_budgets():
    global budgets
    try:
        with open('budgets.json', 'r') as f:
            budgets = json.load(f)
    except FileNotFoundError:
        budgets = {}


def check_budget_warnings():
    for category, limit in budgets.items():
        total_expense = sum(t.amount for t in transactions if t.category == category and t.type == 'expense')
        if total_expense >= limit * 0.8:
            print(f'Warning: {category} spending at {total_expense} of {limit}')