from sklearn.preprocessing import StandardScaler
from numpy.linalg import svd
from sklearn.decomposition import PCA
from sklearn.model_selection import KFold, StratifiedKFold, train_test_split, cross_validate, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from urllib.request import urlopen
import json
import plotly.express as px
import math
import pandas as pd
import numpy as np
import plotly 
import streamlit as st

def get_comb():
    comb = pd.read_csv('data.csv')
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
            counties = json.load(response)
    comb['fips'] = comb['fips'].apply(lambda x: math.trunc(x)).astype(str)
    fips = []
    for index, row in comb.iterrows(): 
        if len(row['fips']) == 4: 
            fips.append('0' + row['fips'])
        else: 
            fips.append(row['fips'])
    comb['fips'] = fips
    return counties, comb

def linear_regression():

    counties, comb = get_comb()

    model = LinearRegression()
    X_lin = comb.drop(columns={'fips', 'Result', 'Margin'})
    y_lin = comb['Margin']
    X_lin_train, X_lin_test, y_lin_train, y_lin_test = train_test_split(X_lin,y_lin, test_size=0.1, random_state=8)
    model.fit(X_lin_train, y_lin_train)
    y_pred = model.predict(X_lin_test)
    lin_r2 = model.score(X_lin_test, y_lin_test)
    y_lin_hats = model.predict(X_lin)
    res = []
    for i in y_lin_hats: 
        if i > 0:
            res.append('D')
        else:
            res.append('R')
    comb['Predicted Margin'] = y_lin_hats
    lin_accuracy = np.sum(np.array(res) == comb['Result'])/len(res)
    lin_fig = px.choropleth_mapbox(comb, geojson=counties, locations='fips', color='Predicted Margin',
                           color_continuous_scale="rdbu",
                           range_color=(-1, 1),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=1,
                          )
    return lin_fig, lin_accuracy, lin_r2, y_lin_hats


def logistic_regression(): 

    counties, comb = get_comb()

    log_model = LogisticRegression(solver = 'saga')
    X_log = comb.drop(columns={'fips', 'Result', 'Margin'})
    y_log = comb['Result']
    X_log_train, X_log_test, y_log_train, y_log_test = train_test_split(X_log,y_log, test_size=0.1, random_state=42)
    log_model.fit(X_log_train, y_log_train)
    y_log_pred = log_model.predict(X_log_test)
    y_log_hats = log_model.predict(X_log)
    log_accuracy = np.sum(y_log_pred == y_log_test)/len(y_log_pred)
    comb['Predicted Result'] = y_log_hats
    log_fig = px.choropleth_mapbox(comb, geojson=counties, locations='fips', color='Predicted Result',
                           color_discrete_map={'R':'red',
                                        'D':'Blue',
                                        'T':'Green'},
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           )
    return log_fig, log_accuracy, y_log_hats
