import streamlit as st

if st.experimental_user.email:
    # Get the user's name from the database.
    name = get_name_from_db(st.experimental_user.email)
    st.write('Hello, %s!' % name)
