# 💰 BudgetCLI

A powerful command-line budget tracking tool that helps you manage expenses, generate reports, and track spending patterns.

## ✨ Features

- 📝 Add expenses with categories and notes
- 📊 View expenses filtered by date or category
- 📈 Generate monthly reports in CSV or PDF format
- 📉 Get quick summary statistics
- 🎯 Track spending patterns by category

## 🚀 Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💡 Usage

### Add an Expense
```bash
python budgetcli.py add --amount 50.25 --category groceries --date 2025-03-25 --note "Weekly groceries"
```

### List Expenses
```bash
# List all expenses
python budgetcli.py list

# Filter by category
python budgetcli.py list --category groceries

# Filter by month
python budgetcli.py list --month 2025-03
```

### Generate Reports
```bash
# Generate CSV report
python budgetcli.py report --month 2025-03 --format csv

# Generate PDF report
python budgetcli.py report --month 2025-03 --format pdf
```

### View Summary
```bash
# View summary for current month
python budgetcli.py summary

# View summary for specific month
python budgetcli.py summary --month 2025-03
```

## 📊 Data Storage

Expenses are stored locally in `expenses.csv` with the following format:
```
date,amount,category,note
2025-03-25,50.25,groceries,Weekly groceries
```

## 🛠️ Tech Stack

- Python 3.x
- pandas: Data management and analysis
- fpdf2: PDF report generation
- argparse: Command-line interface

## 📝 License

This project is licensed under the MIT License.
