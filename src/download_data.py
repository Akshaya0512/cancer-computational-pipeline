import requests
from pathlib import Path
from utils import ensure_dir

def download_tcga_expression(output_path="data/raw/tcga_expression.csv"):
    ensure_dir("data/raw")

    url = (
        "https://raw.githubusercontent.com/greenelab/cimr-datasets/master/"
        "tcga/breast_cancer_expression_small.csv"
    )

    r = requests.get(url)
    r.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(r.content)

    print(f"[✓] TCGA data downloaded → {output_path}")

if __name__ == "__main__":
    download_tcga_expression()
