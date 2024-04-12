import streamlit as st

st.header("Contact Me")

with st.form(key="email_forms"):
    user_emails = st.text_input("your email address")
    message = st.text_area("your message")
    button = st.form_submit_button("Submit")