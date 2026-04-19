# src/ml_models.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def train_models(X_train, X_test, y_train, y_test):

    print("[MODEL] Training Random Forest...")
    rf = RandomForestClassifier(n_estimators=300, random_state=42)
    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test)

    print("[MODEL] Training Logistic Regression...")
    lr = LogisticRegression(max_iter=1000)
    lr.fit(X_train, y_train)
    lr_preds = lr.predict(X_test)

    return {
        "rf_model": rf,
        "rf_preds": rf_preds,
        "lr_model": lr,
        "lr_preds": lr_preds,
        "y_test": y_test,
        "X_train": X_train
    }
