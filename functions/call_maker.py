import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def make_call(to):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")

    if not all([account_sid, auth_token, from_number]):
        print("❌ Missing Twilio credentials in .env")
        return

    client = Client(account_sid, auth_token)
    try:
        call = client.calls.create(
            twiml='<Response><Say>This is a test call from your Python app!</Say></Response>',
            to=to,
            from_=from_number
        )
        print(f"✅ Call initiated! SID: {call.sid}")
    except Exception as e:
        print(f"❌ Failed to make call: {e}")
