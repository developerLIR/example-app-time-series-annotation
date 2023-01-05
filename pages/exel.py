import faker 
import pandas as pandas
import streamlit as st

st.write('hello')
# st.write(dir(faker))
# st.code(input())


col1, col2 = st.columns(2)


with col1:
    bt1 = st.button("click to create a list")
    if bt1:
        ls = []
        st.write(ls)


with col2:
    var = st.text_input("write a word")
    if st.button("add element to a list"):
        
        ls.append(var)
        st.write(ls)


try:
    st.markdown("Hello G<h1> How are you </h1>",unsave_allow_html=True)
except:
    st.write('an error occured')