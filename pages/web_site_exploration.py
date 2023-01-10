import streamlit as st
import requests as req

url = st.text_input("type url")

response = req.get(url)

st.write(response.content)

