import streamlit as st
import pandas as pd 

'Testing streamlit visuals'
"Have fun"

df = pd.DataFrame({'month':['jan','feb','march','apr'], 'value':[3,4,55,2]})

st.line_chart(df)
# def viz_test(df):
#         st.code()
# st