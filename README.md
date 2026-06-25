# Budget Tracker

A personal finance tracker that allows users to manage their budgets and track transactions.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/budget-tracker.git
   cd budget-tracker
   ```
2. Install the required packages:
   ```bash
   pip install matplotlib
   ```

## Usage
1. Add transactions by modifying the `budget_data.json` file or implement CLI logic to do so.
2. Run the CLI:
   ```bash
   python cli.py
   ```
3. Generate reports using:
   ```python
   from reports import generate_report
   generate_report(transactions)
   ```
4. Edit `budgets.json` to set your budget categories and limits.
5. Transactions can be saved in `budget_data.json`.

## License
This project is licensed under the MIT License.