import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Car Sales Dashboard", layout="wide")
st.header("Car Sales Dashboard")

# Load Data
df = pd.read_csv("vehicles_us.csv")

st.write("Dataset Overview:", f"{df.shape[0]} cars, {df.shape[1]} features")

# Create visualizations using correct column names
fig_hist = px.histogram(df, x="model_year", y="price", color="condition", 
                       title="Car Price Distribution by Year and Condition")
st.plotly_chart(fig_hist)

fig_bar = px.bar(df, x="condition", y="price", color="condition", 
                title="Car Price Distribution by Condition")
st.plotly_chart(fig_bar)

fig_scatter = px.scatter(df, x="model_year", y="price", color="condition", 
                        title="Car Price vs Year by Condition")
st.plotly_chart(fig_scatter)

if st.checkbox("Show Raw Data"):
    st.dataframe(df)