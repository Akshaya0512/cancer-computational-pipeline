import pandas as pd
from sklearn.preprocessing import StandardScaler
from utils import ensure_dir

def preprocess_expression(in_file="data/raw/tcga_expression.csv",
                          out_file="data/processed/expression_norm.csv"):

    df = pd.read_csv(in_file, index_col=0)

    df = df.loc[:, df.var() > 0]

    scaler = StandardScaler()
    df_scaled = pd.DataFrame(
        scaler.fit_transform(df),
        index=df.index,
        columns=df.columns
    )

    ensure_dir("data/processed")
    df_scaled.to_csv(out_file)

    print(f"[✓] Preprocessed data saved → {out_file}")

if __name__ == "__main__":
    preprocess_expression()
