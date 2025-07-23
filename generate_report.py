import pandas as pd
import os

def save_summary_report(report_path):
    df = pd.read_csv('data/raw/loan-train.csv')
    total = len(df)
    approved = (df['Loan_Status'] == 'Y').sum()
    rejected = (df['Loan_Status'] == 'N').sum()

    report = (
        "Loan Analysis Summary Report\n\n"
        f"Total Records: {total}\n"
        f"Approved Loans: {approved}\n"
        f"Rejected Loans: {rejected}\n"
        f"Approval Rate: {approved / total:.2%}\n"
    )

    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w") as f:
        f.write(report)
    print(f"Report saved to {report_path}")
