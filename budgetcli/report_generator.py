"""
Report Generator - Handles the generation of expense reports in various formats.
"""
from fpdf import FPDF
import pandas as pd

class ReportGenerator:
    """Generates expense reports in various formats."""
    
    def generate_csv(self, expenses: pd.DataFrame, month: str) -> str:
        """Generate a CSV report for the given expenses."""
        filename = f"report_{month}.csv"
        expenses.to_csv(filename, index=False)
        return filename
    
    def generate_pdf(self, expenses: pd.DataFrame, month: str) -> str:
        """Generate a PDF report for the given expenses."""
        filename = f"report_{month}.pdf"
        
        # Create PDF object
        pdf = FPDF()
        pdf.add_page()
        
        # Set up title
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, f"Expense Report - {month}", ln=True, align="C")
        pdf.ln(10)
        
        # Add summary section
        total = expenses["amount"].sum()
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, f"Total Expenses: ${total:.2f}", ln=True)
        pdf.ln(5)
        
        # Add category breakdown
        pdf.cell(0, 10, "Expenses by Category:", ln=True)
        category_totals = expenses.groupby("category")["amount"].sum()
        
        pdf.set_font("Arial", "", 10)
        for category, amount in category_totals.items():
            pdf.cell(0, 8, f"{category}: ${amount:.2f}", ln=True)
        pdf.ln(10)
        
        # Add expense table
        pdf.set_font("Arial", "B", 10)
        columns = ["Date", "Amount", "Category", "Note"]
        col_widths = [30, 30, 40, 90]
        
        # Table header
        for i, col in enumerate(columns):
            pdf.cell(col_widths[i], 10, col, border=1)
        pdf.ln()
        
        # Table data
        pdf.set_font("Arial", "", 10)
        for _, row in expenses.iterrows():
            pdf.cell(30, 10, str(row["date"]), border=1)
            pdf.cell(30, 10, f"${row['amount']:.2f}", border=1)
            pdf.cell(40, 10, str(row["category"]), border=1)
            pdf.cell(90, 10, str(row["note"]), border=1)
            pdf.ln()
        
        # Save the PDF
        pdf.output(filename)
        return filename
