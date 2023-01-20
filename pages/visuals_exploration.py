import streamlit as st
import pandas as pd 

'Testing streamlit visuals'
"Have fun"

df = pd.DataFrame({'value1':[44,1,13,2],\
 'value2':[3,4,55,2]},index=['january','february','march','april'])

st.write(help(pd.DataFrame)) 
st.image('https://images.unsplash.com/photo-1481349518771-20055b2a7b24?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8cmFuZG9tfGVufDB8fDB8fA%3D%3D&w=1000&q=80')
st.line_chart(df)

# def viz_test(df):
#         st.code()
# st