from dataclasses import dataclass
from datetime import datetime

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

def add_transaction(transaction):
    transactions.append(transaction)

def list_transactions():
    return transactions