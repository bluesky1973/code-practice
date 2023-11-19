
import streamlit as st

st.header('st.selectbox')

option = st.selectbox('what is your favorite color?',('Blue','Yellow','Green'))

st.write('Your favorite color is ',option)
