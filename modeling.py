from sklearn.preprocessing import StandardScaler
from numpy.linalg import svd
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold, StratifiedKFold, train_test_split, cross_validate, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

import pandas as pd
import numpy as np
import plotly 

comb = pd.read_csv('data.csv')

def linear_regression():
    model = LinearRegression()
    X = comb.drop(columns={'fips', 'Result', 'Margin'})
    y = comb['Margin']
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=8)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2 = model.score(X_test, y_test)
    y_hats = model.predict(X)
    res = []
    for i in y_hats: 
        if i > 0:
            res.append('D')
        else:
            res.append('R')
    accuracy = np.sum(np.array(res) == comb['Result'])/len(res)
    return accuracy, r2, y_hats


def logistic_regression(): 
    log_model = LogisticRegression(solver = 'saga')
    X = comb.drop(columns={'fips', 'Result', 'Margin'})
    y = comb['Result']
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
    log_model.fit(X_train, y_train)
    y_pred = log_model.predict(X_test)
    y_hats = log_model.predict(X)
    accuracy = np.sum(y_pred == y_test)/len(y_pred)
    return accuracy, y_hats
