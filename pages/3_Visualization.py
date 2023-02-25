import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Product Category Analysis - Visualization")

st.markdown("<br>",unsafe_allow_html=True)

# read the csv file with all columns except the first two (Unnamed columns)
df = pd.read_csv('resources/data/Washing_machine.csv', usecols=lambda col: col not in ['Unnamed: 0','Unnamed: 0.1'])

col1, col2 = st.columns(2)

fig_1 = px.pie(df,'Price_Category',hole=0.5)
fig_1.update_layout(title_text='washing machines for different ranges of sales price', title_x=0.5)
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.bar(df, x='Brand',color='Brand')
fig_2.update_xaxes(categoryorder="sum descending")
fig_2.update_layout(title_text='Bar chart on Brands', title_x=0.5)
col2.plotly_chart(fig_2, use_container_width=True)

st.markdown("<br>",unsafe_allow_html=True)

col1, col2 = st.columns(2)

fig_1 = px.bar(df, x='Type of Load',color = 'Type of Load')
fig_1.update_yaxes(categoryorder="sum ascending")
fig_1.update_layout(title_text='Washing Machine Distribution by Type of Washing', title_x=0.5)
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.scatter(df, x='Capacity in kgs',y='Sale_Price')
fig_2.update_xaxes(categoryorder="sum descending")
fig_2.update_layout(title_text='Capacity vs Sale price', title_x=0.5)
col2.plotly_chart(fig_2, use_container_width=True)