import streamlit as st
import pandas as pd 
import numpy as np 
import plotly
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
from urllib.request import urlopen
import plotly.express as px

import explore
import models
import theory

st.set_page_config()

st.sidebar.title('Pages')

# page = explore

if 'page' not in st.session_state:
    st.session_state.page = explore

exp = st.sidebar.button("Explore the data")
if exp: 
    st.session_state.page = explore

mod = st.sidebar.button("Shankara's Models")
if mod: 
    st.session_state.page = models

thr = st.sidebar.button("Theory")
if thr: 
    st.session_state.page = theory

st.session_state.page.app()