import streamlit as st
import pandas as pd 

'Testing streamlit visuals'
"Have fun"

df = pd.DataFrame({'value1':[44,1,13,2],\
 'value2':[3,4,55,2]})

st.line_chart(df)
# def viz_test(df):
#         st.code()
# st