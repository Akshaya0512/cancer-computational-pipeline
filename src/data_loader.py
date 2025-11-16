# src/data_loader.py
import pandas as pd

def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    Placeholder function for cancer datasets.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded {len(df)} rows from {file_path}")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
