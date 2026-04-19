# src/data_loader.py

import pandas as pd

def load_data(expr_file, label_file):
    """
    Load gene expression matrix and labels.

    Returns:
        X: features (gene expression)
        y: labels (cancer subtype)
    """

    X = pd.read_csv(expr_file, index_col=0)
    y = pd.read_csv(label_file)["subtype"]

    print(f"[DATA] X shape: {X.shape}")
    print(f"[DATA] y shape: {y.shape}")

    return X, y
