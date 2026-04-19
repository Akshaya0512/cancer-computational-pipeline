# src/preprocessing.py

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def preprocess_data(X, y):
    """
    Clean + split + scale data
    """

    # Align missing values
    X = X.dropna()
    y = y.loc[X.index]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # Normalize (important for gene expression)
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    print("[PREPROCESS] Completed")

    return X_train, X_test, y_train, y_test, scaler
