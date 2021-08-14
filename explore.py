import streamlit as st
import pandas as pd 
import numpy as np 
import plotly
import plotly.figure_factory as ff
import geopandas
import matplotlib.pyplot as plt
from urllib.request import urlopen
import json
import plotly.express as px
import math

def app():

    with st.container():
        st.title("Shankara Predicts Elections")
        st.header("Explore the data")
        st.write(""" Select "Results" to view county-level results from the 2020 presidential race. 
        Select "Variable" to view how any feature in the data set distributes across the nation. 
         """)

    comb = pd.read_csv('data.csv')
    variables = list(comb.columns)

    comb['fips'] = comb['fips'].apply(lambda x: math.trunc(x)).astype(str)
    fips = []
    for index, row in comb.iterrows(): 
        if len(row['fips']) == 4: 
            fips.append('0' + row['fips'])
        else: 
            fips.append(row['fips'])
    comb['fips'] = fips

    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    choose = st.selectbox('Choose', ['Election', 'Variable'])

    if choose == 'Election':
        map = st.selectbox('Select map', ['Presidential'])
        dep = 'Margin'
    else:
        map = st.selectbox('Select map', variables)
        dep = map


    with st.container(): 
        fig = px.choropleth_mapbox(comb, geojson=counties, locations='fips', color=dep,
                            color_continuous_scale="rdbu",
                            mapbox_style="carto-positron",
                            zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                            opacity=0.5,
                            )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        st.plotly_chart(fig,)