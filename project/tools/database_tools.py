import numpy as np
import pandas as pd

def load_csv(file_path=None, filename=None, path=None, table=None, df=None, filepath=None, **kwargs):
    fp = file_path or filename or path or table or filepath
    return pd.read_csv(fp)

def select_columns(df, columns, **kwargs):
    return df[columns]

def filter_rows(df, condition, **kwargs):
    return df.query(condition)

def show_head(df=None, num_rows=5, n=None, dataframe=None, rows=None, **kwargs):
    d = df if df is not None else dataframe
    n_val = n if n is not None else (rows if rows is not None else num_rows)
    return d.head(int(n_val))