"""
This is a boilerplate pipeline 'distribution'
generated using Kedro 0.18.3
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def distribution(df1: pd.DataFrame):
    #Divide the data into decile
    df1['Decile'] = pd.qcut(df1['probability'], 10, labels=[i for i in range (10, 0, -1)])

    #Calculate the actual churn in each decile
    res = pd.crosstab(df1['Decile'], df1['label'])[1].reset_index().rename(columns = {1: 'Number of Responses'})
    lg = df1['Decile'].value_counts(sort = False).reset_index().rename(columns = {'Decile': 'Number of Cases', 'index': 'Decile'})
    lg = pd.merge(lg, res, on = 'Decile').sort_values(by = 'Decile', ascending = False).reset_index(drop = True)
    lg['Acquisition Rate'] = np.round(lg['Number of Responses']/lg['Number of Cases']*100, 2)

    #Calculate the cumulative
    lg['Cumulative Responses'] = lg['Number of Responses'].cumsum()
    #Calculate the percentage of positive in each decile compared to the total nu
    lg['% of Events'] = np.round(((lg['Number of Responses']/lg['Number of Responses'].sum())*100),2)
    #Calculate the Gain in each decile
    lg['Gain'] = lg['% of Events'].cumsum()
    lg['Decile'] = lg['Decile'].astype('int')
    lg['lift'] = np.round((lg['Gain']/(lg['Decile']*10)),2)
    return df1, lg

def bar(df:pd.DataFrame):
    fig = plt.figure(figsize = (10, 5))
    plt.barh(df['Decile'], df['Acquisition Rate'], color ='blue')
    plt.xlabel("Acquisition Rate")
    plt.ylabel("Decile")
    plt.title("Distribution of Customer Acquisition")
    plt.show()