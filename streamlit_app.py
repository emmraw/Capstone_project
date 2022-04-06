import pandas as pd
import streamlit as st

import plotly.express as px
import datetime
import time
"""
# Welcome to the Cobbles shop app!
"""
#st.title("Cobbles App")
st.sidebar.header('Widgets')

add_selectbox1 = st.sidebar.date_input(
     "Enter the date you wish to predict",
     datetime.date(2020,3,21))

add_selectbox2 = st.sidebar.selectbox(
     "What is today's weather like?",
     ('Sunny', 'Cloudy', 'Rainy'))

add_selectbox3 = st.sidebar.selectbox(
    "Is it a bank holiday?",
    ("No","Yes"))

add_selectbox4 = st.sidebar.selectbox(
    "Is there a special event?",
    ("No","Yes"))
