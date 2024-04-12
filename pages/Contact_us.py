import streamlit as st
from Send_email import Send_email
st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("your email address")
    raw_message = st.text_area("your message")
    message = f"""\
Subject: new message from: {user_email} 

from{user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        Send_email(message)
        st.info("your email was sent successfully")