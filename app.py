import streamlit as st
import pandas as pd
import plotly.express as px

set.set_page_config(page_title="Data Dashboard", layout="wide")
st.header("Data Dashboard")

#Load Data
df = pd.read_csv("D:\.MAGUS ARCHIEVE\.Main Projects\Workshop\streamdash-v3\vehicles_us.csv")