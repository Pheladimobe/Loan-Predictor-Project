import pandas as pd
import os

def create_pivot_tables(input_path, output_path):
    # Load cleaned data
    df = pd.read_excel(input_path)

    # Create a pivot table: Average LoanAmount by Education and Gender
    pivot = pd.pivot_table(df, values='LoanAmount', index=['Education'], columns=['Gender'], aggfunc='mean')

    # Save pivot to Excel
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pivot.to_excel(output_path)
    print(f"Pivot table saved to {output_path}")
