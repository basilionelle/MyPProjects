#!/usr/bin/env python3
"""
BudgetCLI - A command-line budget tracking tool.
"""
import argparse
from datetime import datetime
from budget_manager import BudgetManager

def setup_parser():
    """Configure and return the argument parser."""
    parser = argparse.ArgumentParser(
        description="BudgetCLI - Track your expenses from the command line"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add expense command
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--amount", type=float, required=True, help="Expense amount")
    add_parser.add_argument("--category", type=str, required=True, help="Expense category")
    add_parser.add_argument("--date", type=str, help="Expense date (YYYY-MM-DD)", default=datetime.now().strftime("%Y-%m-%d"))
    add_parser.add_argument("--note", type=str, help="Optional note", default="")
    
    # List expenses command
    list_parser = subparsers.add_parser("list", help="List expenses")
    list_parser.add_argument("--category", type=str, help="Filter by category")
    list_parser.add_argument("--month", type=str, help="Filter by month (YYYY-MM)")
    
    # Report command
    report_parser = subparsers.add_parser("report", help="Generate expense report")
    report_parser.add_argument("--month", type=str, required=True, help="Month to generate report for (YYYY-MM)")
    report_parser.add_argument("--format", type=str, choices=["csv", "pdf"], default="csv", help="Report format")
    
    # Summary command
    summary_parser = subparsers.add_parser("summary", help="Show expense summary")
    summary_parser.add_argument("--month", type=str, help="Month to summarize (YYYY-MM)")
    
    return parser

def main():
    """Main entry point for the CLI application."""
    parser = setup_parser()
    args = parser.parse_args()
    
    budget_manager = BudgetManager()
    
    if args.command == "add":
        budget_manager.add_expense(args.amount, args.category, args.date, args.note)
        print(f"Added expense: ${args.amount:.2f} for {args.category}")
    
    elif args.command == "list":
        expenses = budget_manager.list_expenses(category=args.category, month=args.month)
        if not expenses.empty:
            print("\nExpenses:")
            print(expenses.to_string(index=False))
        else:
            print("No expenses found.")
    
    elif args.command == "report":
        filepath = budget_manager.generate_report(args.month, args.format)
        print(f"Report generated: {filepath}")
    
    elif args.command == "summary":
        summary = budget_manager.get_summary(args.month)
        print("\nExpense Summary:")
        print(f"Total Spent: ${summary['total']:.2f}")
        print("\nBy Category:")
        for category, amount in summary['by_category'].items():
            print(f"{category}: ${amount:.2f}")
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
