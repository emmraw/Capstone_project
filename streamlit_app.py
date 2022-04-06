import pandas as pd
import streamlit as st

import plotly.express as px
import datetime
import time
"""
# Welcome to the Cobbles shop app!
"""
st.title("Cobbles App")
st.header('Widgets')

d = st.date_input(
     "Enter the date you wish to predict",
     datetime.date(2020,3,21))
st.write("You chose:", d)

option1 = st.selectbox(
     "What is today's weather like?",
     ('Sunny', 'Cloudy', 'Rainy'))
     
option2 = st.selectbox("Is it a bank holiday today?",('No','Yes'))
                     
option3 = st.selectbox("Is there a special event today?",('No','Yes'))
     
st.write("You chose: ", option1, option2, option3)

add_selectbox = st.sidebar.selectbox(
    "Is it a bank holiday?",
    ("No","Yes"))

add_selectbox = st.sidebar.selectbox(
    "Is there a special event?",
    ("No","Yes"))
