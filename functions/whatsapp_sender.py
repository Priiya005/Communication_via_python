# functions/whatsapp_sender.py
import webbrowser
import pyautogui
import time
import urllib.parse

def send_whatsapp_message(phone, message):
    encoded_msg = urllib.parse.quote(message)
    url = f"https://web.whatsapp.com/send?phone={phone}&text={encoded_msg}"
    webbrowser.open(url)
    time.sleep(15)  # wait for page load
    pyautogui.press("enter")
    return "WhatsApp message sent successfully!"
