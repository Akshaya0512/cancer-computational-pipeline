from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.ml_models import train_models
from src.analysis import evaluate_model, top_features

def main():

    X, y = load_data(
        "data/processed/expression_norm.csv",
        "data/raw/tcga_labels_small.csv"
    )

    X_train, X_test, y_train, y_test, scaler = preprocess_data(X, y)

    results = train_models(X_train, X_test, y_train, y_test)

    print("\nRandom Forest:")
    evaluate_model(results["y_test"], results["rf_preds"])

    print("\nLogistic Regression:")
    evaluate_model(results["y_test"], results["lr_preds"])

    top_features(results["rf_model"], results["X_train"].columns)

if __name__ == "__main__":
    main()
