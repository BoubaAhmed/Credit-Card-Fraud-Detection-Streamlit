import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is your first Streamlit app.')

# Add a slider
x = st.slider('Select a value')
st.write('You selected:', x)
