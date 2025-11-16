# src/analysis.py
def basic_stats(df, column):
    """
    Compute basic statistics for a numeric column.
    """
    if df is None or column not in df.columns:
        print(f"Column {column} not found")
        return
    stats = {
        "mean": df[column].mean(),
        "median": df[column].median(),
        "max": df[column].max(),
        "min": df[column].min()
    }
    return stats
