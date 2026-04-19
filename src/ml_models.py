# src/ml_models.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def train_models(X_train, X_test, y_train, y_test):
    """
    Train multiple machine learning models on gene expression data.

    Parameters:
        X_train, X_test: Feature data
        y_train, y_test: Labels

    Returns:
        dict: Trained models and predictions
    """

    print("[3] Training Random Forest...")
    rf_model = RandomForestClassifier(n_estimators=300, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_preds = rf_model.predict(X_test)

    print("[4] Training Logistic Regression...")
    lr_model = LogisticRegression(max_iter=1000)
    lr_model.fit(X_train, y_train)
    lr_preds = lr_model.predict(X_test)

    print("[✓] Models trained successfully!")

    return {
        "rf_model": rf_model,
        "rf_preds": rf_preds,
        "lr_model": lr_model,
        "lr_preds": lr_preds,
        "y_test": y_test,
        "X_train": X_train
    }
