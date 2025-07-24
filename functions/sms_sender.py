import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def send_sms(to, message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")

    if not all([account_sid, auth_token, from_number]):
        print("❌ Missing Twilio credentials in .env")
        return

    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body=message,
            from_=from_number,
            to=to
        )
        print(f"✅ SMS sent successfully! SID: {message.sid}")
    except Exception as e:
        print(f"❌ Failed to send SMS: {e}")
