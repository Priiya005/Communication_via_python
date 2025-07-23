# app.py
import streamlit as st
import json
from functions.whatsapp_sender import send_whatsapp_message
from functions.email_sender import send_email
from functions.linkedin_poster import post_on_linkedin
from functions.sms_sender import send_sms
from functions.call_maker import make_phone_call

st.set_page_config(page_title="Communication via Python", layout="centered")

st.title("📡 Communication via Python")

menu = st.selectbox("Choose a Communication Method", [
    "Send WhatsApp Message",
    "Send Email",
    "Send SMS",
    "Make Phone Call",
    "Post on LinkedIn"
])

if menu == "Send WhatsApp Message":
    number = st.text_input("Receiver WhatsApp Number (with country code)")
    msg = st.text_area("Enter message")
    if st.button("Send"):
        result = send_whatsapp_message(number, msg)
        st.success(result)

elif menu == "Send Email":
    sender = st.text_input("Sender Email")
    password = st.text_input("Sender Email Password", type="password")
    receiver = st.text_input("Receiver Email")
    subject = st.text_input("Subject")
    msg = st.text_area("Enter Message")
    if st.button("Send Email"):
        result = send_email(sender, password, receiver, subject, msg)
        st.success(result)

elif menu == "Send SMS":
    number = st.text_input("Enter Mobile Number (with country code if required):")
    msg = st.text_area("Enter your message:")
    if st.button("Send SMS"):
        if number and msg:
            result = send_sms(number, msg)
            st.success(result)
        else:
            st.warning("📌 Please enter both number and message.")


elif menu == "Make Phone Call":
    st.markdown("### 📞 Make a Phone Call using Twilio")
    to_number = st.text_input("Enter receiver phone number with country code (e.g., +91XXXXXXXXXX)")
    if st.button("Make Call", type="primary"):
        if to_number.strip():
            result = make_phone_call(to_number)
            st.info(result)
        else:
            st.warning("Please enter a valid phone number.")


elif menu == "Post on LinkedIn":
    msg = st.text_area("Enter your post content")
    if st.button("Post"):
        result = post_on_linkedin(msg)
        st.success(result)
