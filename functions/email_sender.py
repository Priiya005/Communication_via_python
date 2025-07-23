# functions/email_sender.py
import yagmail

def send_email(sender_email, sender_password, receiver_email, subject, message):
    try:
        yag = yagmail.SMTP(user=sender_email, password=sender_password)
        yag.send(to=receiver_email, subject=subject, contents=message)
        return "Email sent successfully!"
    except Exception as e:
        return f"❌ Failed: {e}"
