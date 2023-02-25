import streamlit as st
import pandas as pd
import io
from PIL import Image, ImageDraw, ImageOps

st.set_page_config(
    page_title="Portfolio",
    page_icon=":sunglasses:")

# Title and Introduction
st.title("Ramesh Isukapalli - Personal Portfolio")

st.markdown("<br>",unsafe_allow_html=True)
st.markdown("<br>",unsafe_allow_html=True)

st.subheader("Hello there!! 👋 I'm a Data Science Trainee")
st.write("I'm enthusiastic in Data Science field and Statistics. I would love to be in discussions involving the mentioned two fields. I'm also skilled in developing dashboards using Tableau (Data Visualization)")


st.markdown("<br>",unsafe_allow_html=True)
# Contact Section
st.header("Contact Me")
st.write("Feel free to connect with me on any of the below platforms or send me an email at rameshisukapalli5@gmail.com. I'd love to hear from you!")


# Define the URLs for your social media profiles
instagram_url = "https://www.instagram.com/_rameshisukapalli/"
linkedin_url = "https://www.linkedin.com/in/rameshisukapalli2802/"
github_url = "https://github.com/Ramesh-Isukapalli/"

# Container to hold the buttons
container = st.container()

col1, col2, col3 = container.columns(3)

with col1:
    st.markdown(f'<a href="{linkedin_url}" target="_blank">Connect on LinkedIn</a>',unsafe_allow_html=True)

with col2:
    st.markdown(f'<a href="{instagram_url}" target="_blank">Connect on Instagram</a>',unsafe_allow_html=True)

with col3:
    st.markdown(f'<a href="{github_url}" target="_blank">Connect on Github</a>',unsafe_allow_html=True)

