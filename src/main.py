# main.py

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.ml_models import train_models
from src.analysis import evaluate_model, top_features


def main():
    print("=== Cancer ML Pipeline ===")

    # Step 1: Load Data
    X, y = load_data(
        "data/processed/expression_norm.csv",
        "data/raw/tcga_labels_small.csv"
    )

    # Step 2: Preprocess
    X_train, X_test, y_train, y_test, scaler = preprocess_data(X, y)

    # Step 3: Train Models
    results = train_models(X_train, X_test, y_train, y_test)

    # Step 4: Evaluate Random Forest
    print("\n--- Random Forest Results ---")
    evaluate_model(results["y_test"], results["rf_preds"])

    # Step 5: Evaluate Logistic Regression
    print("\n--- Logistic Regression Results ---")
    evaluate_model(results["y_test"], results["lr_preds"])

    # Step 6: Feature Importance
    print("\n--- Top Genes (Feature Importance) ---")
    top_features(results["rf_model"], results["X_train"].columns)

    print("\n=== Pipeline Complete ===")


if __name__ == "__main__":
    main()
