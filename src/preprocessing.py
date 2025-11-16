# src/preprocessing.py
def drop_missing(df, columns=None):
    """
    Drop rows with missing values in specified columns.
    """
    if df is None:
        print("No DataFrame provided")
        return None
    return df.dropna(subset=columns)

def preview(df, n=5):
    """Print first n rows of DataFrame"""
    if df is not None:
        print(df.head(n))
