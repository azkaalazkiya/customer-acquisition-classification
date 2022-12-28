"""
This is a boilerplate pipeline 'modeling'
generated using Kedro 0.18.3
"""

from sklearn.model_selection import train_test_split, GridSearchCV
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.metrics import make_scorer, roc_auc_score
from sklearn.preprocessing import LabelEncoder

def split_data(df:pd.DataFrame):
    X_clean = df.loc[:, df.columns != 'label']
    y_clean = df.label
    X_train, y_train, X_test, y_test = train_test_split(X_clean, y_clean, train_size=0.8, random_state=42)
    return X_train, y_train, X_test, y_test


def model_acq(X_train:pd.DataFrame, X_test:pd.DataFrame, y_train:pd.DataFrame, y_test:pd.DataFrame):
    """Machine learning process consists of 
    data training, and data testing process (i.e. prediction) with Catboost Algorithm
    """
    # prepare a new DataFrame
    training = pd.DataFrame(X_train).copy()
    testing = pd.DataFrame(X_test).copy()
    
    xgb_clf = xgb.XGBClassifier()
    xgb_clf = xgb_clf.fit(X_train, y_train)
    
    prediction_train = xgb_clf.predict(X_train)
    probability_train = xgb_clf.predict_proba(X_train)
    training['prediction'] = prediction_train
    training['probability'] = probability_train[:,1] 

    prediction_test = xgb_clf.predict(X_test)
    probability_test = xgb_clf.predict_proba(X_test)
    testing['prediction'] = prediction_test
    testing['probability'] = probability_test[:,1]
          
    # add the acquisition and target class into dataframe as validation data
    training['label'] = y_train
    testing['label'] = y_test

    return training, testing