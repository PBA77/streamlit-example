import streamlit as st

if st.experimental_user.email:
    st.write('Hello, %s!' % st.experimental_user.email)
else:
    st.write('Hello, unauthorized!')
