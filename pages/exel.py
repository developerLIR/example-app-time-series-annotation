import faker 
import pandas as pd
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
        
        ls.append(str(var))
        st.write(ls)
try:
    st.markdown("<h1> How are you </h1>",unsave_allow_html=True)
except:
    st.write('an error occured')

try:
    st.markdown("A bit of markdown")
except:
    st.write('an error occured')

fake = faker.Faker()
df = pd.DataFrame({id:[fake.name() for i in range(30)]})
df2 = pd.DataFrame({'month':["fake.name() for i in range(30)",'dfdf'],'value':[]})
x = df2
'this is write method'
st.write(x)
'this is dataframe method'
st.table(x)
st.dataframe(x)

"this is table method"

try:
    st.code('st.table(dir(faker.Faker))')
    st.table(dir(faker.Faker))
except:
    'exception'
try:
    st.code('st.write(dir(faker.Faker))')
    st.write(dir(faker.Faker))
except:
    'exception'


