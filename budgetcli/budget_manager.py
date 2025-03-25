"""
Budget Manager - Handles the core logic for expense tracking and data management.
"""
import os
from datetime import datetime
import pandas as pd
from report_generator import ReportGenerator

class BudgetManager:
    """Manages budget tracking operations and data storage."""
    
    def __init__(self, file_path="expenses.csv"):
        """Initialize the budget manager with the data file path."""
        self.file_path = file_path
        self.report_generator = ReportGenerator()
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        """Create the expenses file if it doesn't exist."""
        if not os.path.exists(self.file_path):
            df = pd.DataFrame(columns=["date", "amount", "category", "note"])
            df.to_csv(self.file_path, index=False)
    
    def add_expense(self, amount: float, category: str, date: str, note: str = ""):
        """Add a new expense to the tracking system."""
        try:
            # Validate date format
            datetime.strptime(date, "%Y-%m-%d")
            
            new_expense = pd.DataFrame({
                "date": [date],
                "amount": [amount],
                "category": [category.lower()],
                "note": [note]
            })
            
            if os.path.exists(self.file_path):
                expenses = pd.read_csv(self.file_path)
                expenses = pd.concat([expenses, new_expense], ignore_index=True)
            else:
                expenses = new_expense
                
            expenses.to_csv(self.file_path, index=False)
            return True
        except ValueError as e:
            print(f"Error adding expense: {str(e)}")
            return False
    
    def list_expenses(self, category=None, month=None):
        """List expenses with optional filtering."""
        if not os.path.exists(self.file_path):
            return pd.DataFrame()
            
        expenses = pd.read_csv(self.file_path)
        
        if expenses.empty:
            return expenses
            
        # Apply filters
        if category:
            expenses = expenses[expenses["category"].str.lower() == category.lower()]
        
        if month:
            expenses["date"] = pd.to_datetime(expenses["date"])
            expenses = expenses[expenses["date"].dt.strftime("%Y-%m") == month]
            expenses["date"] = expenses["date"].dt.strftime("%Y-%m-%d")
            
        return expenses.sort_values("date", ascending=False)
    
    def get_summary(self, month=None):
        """Generate a summary of expenses."""
        expenses = self.list_expenses(month=month)
        
        if expenses.empty:
            return {"total": 0.0, "by_category": {}}
            
        total = expenses["amount"].sum()
        by_category = expenses.groupby("category")["amount"].sum().to_dict()
        
        return {
            "total": total,
            "by_category": by_category
        }
    
    def generate_report(self, month: str, format: str = "csv"):
        """Generate an expense report for the specified month."""
        expenses = self.list_expenses(month=month)
        
        if expenses.empty:
            print(f"No expenses found for {month}")
            return None
            
        if format == "csv":
            return self.report_generator.generate_csv(expenses, month)
        elif format == "pdf":
            return self.report_generator.generate_pdf(expenses, month)
        else:
            raise ValueError(f"Unsupported format: {format}")
