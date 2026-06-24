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

def save_transactions():
    with open('budget_data.json', 'w') as f:
        json.dump([t.__dict__ for t in transactions], f, default=str)

def add_transaction(transaction):
    transactions.append(transaction)
    save_transactions()

def list_transactions():
    return transactions

load_transactions()