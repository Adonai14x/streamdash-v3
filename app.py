from numpy import histogram
import streamlit as st
import pandas as pd
import plotly.express as px

set.set_page_config(page_title="Data Dashboard", layout="wide")
st.header("Data Dashboard")

#Load Data
df = pd.read_csv("D:\.MAGUS ARCHIEVE\.Main Projects\Workshop\streamdash-v3\vehicles_us.csv")

st.write("Car Data Dashboard", df.head())

fig_hist = px.histogram(df, x="year", y="price", color="brand", title="Car Price Distribution by Year")
st.plotly_chart(fig_hist)

fig_bar = px.bar(df, x="brand", y="price", color="brand", title="Car Price Distribution by Brand")
st.plotly_chart(fig_bar)

fig_scatter = px.scatter(df, x="year", y="price", color="brand", title="Car Price Distribution by Year")
st.plotly_chart(fig_scatter)

if st.checkbox("Show Raw Data"):
    st.dataframe(df)