"""
This is a boilerplate pipeline 'data_preprocessing'
generated using Kedro 0.18.3
"""
import pandas as pd
from mrmr import mrmr_classif

def drop_column(df:pd.DataFrame):
    #Menghapus fitur dengan type data kategori
    datafull = df.select_dtypes(exclude=['object', 'bool'])
    datafull = datafull.loc[:, datafull.columns != 'index']
    return datafull

def mrmr_selection(df:pd.DataFrame):
    # create some pandas data
    X = df.loc[:, df.columns != 'label']
    y = df.label

    # select top 10 features using mRMR
    selected_features = mrmr_classif(X=X, y=y, K=12)
    data_mrmr = df[df.columns.intersection(selected_features)]
    data_clean = pd.concat([data_mrmr, df.label], axis=1)
    return data_clean

