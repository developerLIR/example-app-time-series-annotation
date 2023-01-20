import streamlit as st
import pandas as pd 

'Testing streamlit visuals'
"Have fun"

df = pd.DataFrame({'value1':[44,1,13,2],\
 'value2':[3,4,55,2]},index=['january','february','march','april'])

 

st.line_chart(df)
st.write(help(st.line_chart()))
# def viz_test(df):
#         st.code()
# st