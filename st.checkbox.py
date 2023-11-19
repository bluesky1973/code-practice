import streamlit as st

st.header("st.checkbox")

st.write("what would you like order?")

milk = st.checkbox('Milk')
coffee = st.checkbox('Coffee')
coke = st.checkbox('Coke')

if milk:
    st.write("Great!,Here's some more")

if coffee:
    st.write("Here's some coffee")

if coke:
    st.write("Here you go")