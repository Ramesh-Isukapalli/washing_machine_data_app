import streamlit as st
import pandas as pd
import os
import io

st.set_page_config(
    page_title="Washing Machines",
    page_icon=":Chart:")


st.title("Product Category Analysis - Washing Machines")



# read the csv file with all columns except the first two (Unnamed columns)
df = pd.read_csv('resources/data/Washing_machine.csv', usecols=lambda col: col not in ['Unnamed: 0','Unnamed: 0.1'])


data_info = st.radio('Click on the detail of data frame you want view:',
                      ('Shape', 'Head', 'Tail', 'Columns', 'Info', 'Descriptive Statistics'),
                      horizontal=True)

if data_info == 'Shape':
    st.write(f"Number rows in data frame: {df.shape[0]}")
    st.write(f"Number columns in data frame: {df.shape[1]}")
elif data_info == 'Head':
    st.write(df.head())
elif data_info == 'Tail':
    st.write(df.tail())
elif data_info == 'Columns':
    st.write(', '.join(df.columns.tolist()))
elif data_info == 'Info':
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
else:
    st.write(df.describe())


@st.cache
def convert_df(df):
    #IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.markdown("<br>",unsafe_allow_html=True)

col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.download_button(
     label="Download Dataset",
     data=csv,
     file_name='my_pubs.csv',
     mime='text/csv',
 )
