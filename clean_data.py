import pandas as pd
import os

def clean_data(input_path, output_path):
    # Load CSV
    df = pd.read_csv(input_path)

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Convert data types if needed
    df['LoanAmount'] = pd.to_numeric(df['LoanAmount'], errors='coerce')

    # Fill any remaining NaNs with 0
    df.fillna(0, inplace=True)

    # Save to Excel
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_excel(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
