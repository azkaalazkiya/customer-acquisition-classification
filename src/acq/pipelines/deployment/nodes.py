"""
This is a boilerplate pipeline 'deployment'
generated using Kedro 0.18.4
"""
#!pip install xgboost
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb

def proba(df:pd.DataFrame, X_clean:pd.DataFrame, y_clean:pd.DataFrame):
    X_clean_oot = df.loc[:, df.columns != 'label']
    X_clean_oot = X_clean_oot[X_clean_oot.columns.intersection(["fea_2","fea_15","fea_28","fea_34","fea_63","fea_71","fea_86","fea_96","fea_99","fea_114","fea_124","fea_150"])]
    y_clean_oot = df.label
    xgb_clf = xgb.XGBClassifier()
    xgb_clf = xgb_clf.fit(X_clean, y_clean)

    probability_clean = xgb_clf.predict_proba(X_clean_oot)
    X_clean_oot['probability'] = probability_clean[:,1] 
    data_clean_fix = pd.concat([X_clean_oot,y_clean_oot], axis=1)
    return data_clean_fix