# src/analysis.py

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np


def evaluate_model(y_test, preds, name="Model"):
    """
    Evaluate classification performance
    """

    acc = accuracy_score(y_test, preds)
    cm = confusion_matrix(y_test, preds)

    print(f"\n=== {name} ===")
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, preds))
    print("Confusion Matrix:\n", cm)

    return acc


def top_features(model, feature_names, top_n=10):
    """
    Feature importance (gene importance ranking)
    """

    if not hasattr(model, "feature_importances_"):
        print("[FEATURES] Not supported for this model")
        return

    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1][:top_n]

    print("\n=== Top Genes ===")
    for i in indices:
        print(f"{feature_names[i]}: {importances[i]:.4f}")
