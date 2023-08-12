import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Sale Prediction App

This app predicts the **number of sale** based on the method of advertising used.
""")

st.sidebar.header('User Input Parameters')
