import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header("st.write")

#example1
st.write('hello, *World!* :sunglasses:')

#example2
st.write(4567)

#example3
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})
st.write(df)

#example 4
st.write('Below is a DataFrame:',df,'above is a dataframe.')

#example 5
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c',color='c',tooltip=['a','b','c'])

st.write(c)




