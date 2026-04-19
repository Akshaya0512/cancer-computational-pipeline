# src/analysis.py

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

def basic_stats(df, column):
    """
    Compute basic statistics for a numeric column.

    Parameters:
        df (pd.DataFrame): Input dataset
        column (str): Column name

    Returns:
        dict: Summary statistics
    """
    if df is None or column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataframe")

    return {
        "mean": df[column].mean(),
        "median": df[column].median(),
        "max": df[column].max(),
        "min": df[column].min(),
        "std": df[column].std()
    }


def evaluate_model(y_test, predictions):
    """
    Evaluate model performance.

    Parameters:
        y_test: True labels
        predictions: Model predictions

    Returns:
        dict: Evaluation metrics
    """
    acc = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)

    print("\n=== Model Evaluation ===")
    print(f"Accuracy: {acc:.4f}")
    print("\nClassification Report:")
    print(report)
    print("\nConfusion Matrix:")
    print(cm)

    return {
        "accuracy": acc,
        "confusion_matrix": cm
    }


def top_features(model, feature_names, n=10):
    """
    Get most important features (for models like Random Forest).

    Parameters:
        model: Trained model with feature_importances_
        feature_names: List of feature names
        n: Number of top features

    Returns:
        list: Top features
    """
    if not hasattr(model, "feature_importances_"):
        print("Model does not support feature importance")
        return []

    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    top = [(feature_names[i], importances[i]) for i in indices[:n]]

    print("\n=== Top Features ===")
    for name, score in top:
        print(f"{name}: {score:.4f}")

    return top
