import json
from storage import load_transactions, save_transactions
from models import Transaction


def main():
    transactions = load_transactions()
    # Implement CLI logic to add/edit transactions
    pass

if __name__ == '__main__':
    main()