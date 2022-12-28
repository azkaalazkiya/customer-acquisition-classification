"""
This is a boilerplate pipeline 'deployment'
generated using Kedro 0.18.4
"""
#!pip install xgboost
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb

def proba(df:pd.DataFrame):
    X_clean = df.loc[:, df.columns != 'label']
    y_clean = df.label
    xgb_clf = xgb.XGBClassifier()
    xgb_clf = xgb_clf.fit(X_clean, y_clean)

    probability_clean = xgb_clf.predict_proba(X_clean)
    X_clean['probability'] = probability_clean[:,1] 
    data_clean_fix = pd.concat([X_clean,y_clean], axis=1)
    return data_clean_fix