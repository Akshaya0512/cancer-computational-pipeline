# src/data_loader.py

import pandas as pd

def load_data(expr_file, label_file):
    """
    Load gene expression data and labels.

    Returns:
        X (DataFrame): Features
        y (Series): Labels
    """
    try:
        X = pd.read_csv(expr_file, index_col=0)
        y = pd.read_csv(label_file)["subtype"]

        print(f"[✓] Loaded expression data: {X.shape}")
        print(f"[✓] Loaded labels: {y.shape}")

        return X, y

    except Exception as e:
        print(f"[✗] Error loading data: {e}")
        return None, None
