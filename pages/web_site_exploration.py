import streamlit as st
import requests as req

url = st.text_input("type url")
if st.button("run"):
    response = req.get(url)
    st.write(response.content)

