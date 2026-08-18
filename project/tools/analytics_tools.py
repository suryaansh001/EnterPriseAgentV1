from scipy import stats

def _resolve_df(dataframe=None, df=None):
    return df if df is not None else dataframe

def calculate_mean(dataframe=None, column=None, column_name=None, col=None, df=None, **kwargs):
    d = _resolve_df(dataframe, df)
    c = column or column_name or col
    return d[c].mean()

def calculate_sum(dataframe=None, column=None, column_name=None, col=None, df=None, **kwargs):
    d = _resolve_df(dataframe, df)
    c = column or column_name or col
    return d[c].sum()

def correlation_matrix(dataframe=None, df=None, **kwargs):
    d = _resolve_df(dataframe, df)
    return d.select_dtypes(include="number").corr()

def t_test(dataframe=None, column1=None, column2=None, col1=None, col2=None, df=None, **kwargs):
    d = _resolve_df(dataframe, df)
    c1 = column1 or col1
    c2 = column2 or col2
    return stats.ttest_ind(d[c1], d[c2])

def z_score(dataframe=None, column=None, column_name=None, col=None, df=None, **kwargs):
    d = _resolve_df(dataframe, df)
    c = column or column_name or col
    return (d[c] - d[c].mean()) / d[c].std()
