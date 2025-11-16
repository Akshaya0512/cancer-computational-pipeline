import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_classifier(expr_file="data/processed/expression_norm.csv",
                     label_file="data/raw/tcga_labels_small.csv"):

    X = pd.read_csv(expr_file, index_col=0)
    y = pd.read_csv(label_file)["subtype"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = RandomForestClassifier(n_estimators=300)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)

    print("[✓] Model Results:")
    print(classification_report(y_test, preds))

if __name__ == "__main__":
    train_classifier()
