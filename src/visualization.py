# src/visualize.py
import matplotlib.pyplot as plt

def plot_column(df, column):
    """
    Create a simple histogram of a column.
    """
    if df is None or column not in df.columns:
        print(f"Column {column} not found")
        return
    df[column].hist()
    plt.title(f"Distribution of {column}")
    plt.show()
