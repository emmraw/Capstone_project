import pandas as pd
import streamlit as st

import plotly.express as px
import datetime
import time
"""
# Welcome to the Cobbles shop app!
"""
#st.title("Cobbles App")
st.header('Widgets')

add_selectbox = st.date_input(
     "Enter the date you wish to predict",
     datetime.date(2020,3,21))

add_selectbox = st.selectbox(
     "What is today's weather like?",
     ('Sunny', 'Cloudy', 'Rainy'))

add_selectbox = st.sidebar.selectbox(
    "Is it a bank holiday?",
    ("No","Yes"))

add_selectbox = st.sidebar.selectbox(
    "Is there a special event?",
    ("No","Yes"))
