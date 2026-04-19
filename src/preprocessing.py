# src/preprocessing.py

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocess_data(X, y, test_size=0.2):
    """
    Clean and prepare data for ML.

    Steps:
    - Remove missing values
    - Split train/test
    - Normalize features
    """

    if X is None or y is None:
        raise ValueError("Invalid input data")

    print("[1] Removing missing values...")
    X = X.dropna()
    y = y.loc[X.index]

    print("[2] Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    print("[3] Normalizing data...")
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("[✓] Preprocessing complete!")

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler
