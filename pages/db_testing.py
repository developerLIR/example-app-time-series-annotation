import streamlit as st

st.write('here you can test your db connection')

if st.button('default'):
    st.write('')

    import pandas as pd
    import sqlalchemy as sa
    url = sa.engine.URL.create(  drivername="postgresql",
    username='analytics',
    password='HRanalytics',
    host='rc1c-fhrb9f1e0l9g611h.mdb.yandexcloud.net',
    port=6432,
    database='hr-analytics')
    engine = sa.create_engine(url,connect_args={'sslmode':'require'})
    orders = pd.read_sql_table('orders',engine)
    st.table(orders)

    