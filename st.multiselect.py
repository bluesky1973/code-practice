
import streamlit as st

st.header('st.multiselect')

option = st.multiselect('what are you favorite color?',['Red','Blue','Pink','Yellow'],['Yellow','Blue'])
st.write('You selected color is ',option)