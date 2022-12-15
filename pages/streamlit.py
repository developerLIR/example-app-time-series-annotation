import streamlit as st

library = st.text_input("type standart library name")

if st.button('show lib'):

    st.table(dir(library))