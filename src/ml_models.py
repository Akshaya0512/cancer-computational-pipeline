# src/ml_models.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def train_models(expr_file="data/processed/expression_norm.csv",
                 label_file="data/raw/tcga_labels_small.csv"):
    """
    Train multiple ML models on gene expression data.
    """

    print("[1] Loading data...")
    X = pd.read_csv(expr_file, index_col=0)
    y = pd.read_csv(label_file)["subtype"]

    print("[2] Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -------------------------------
    # Model 1: Random Forest
    # -------------------------------
    print("[3] Training Random Forest...")
    rf = RandomForestClassifier(n_estimators=300, random_state=42)
    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test)

    # -------------------------------
    # Model 2: Logistic Regression
    # -------------------------------
    print("[4] Training Logistic Regression...")
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)
    lr_preds = lr.predict(X_test)

    print("[✓] Models trained successfully!")

    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "rf_model": rf,
        "rf_preds": rf_preds,
        "lr_model": lr,
        "lr_preds": lr_preds
    }
