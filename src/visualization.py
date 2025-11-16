import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def plot_gene_distribution(file="data/processed/expression_norm.csv", gene="BRCA1"):
    df = pd.read_csv(file, index_col=0)

    if gene not in df.columns:
        print(f"[!] Gene {gene} not in dataset.")
        return

    sns.histplot(df[gene], kde=True)
    plt.title(f"Expression Distribution: {gene}")
    plt.show()

def plot_heatmap(file="data/processed/expression_norm.csv", n_genes=50):
    df = pd.read_csv(file, index_col=0)
    df_sample = df.iloc[:, :n_genes]

    sns.clustermap(df_sample, cmap="viridis")
    plt.show()

if __name__ == "__main__":
    plot_heatmap()
