# functions/linkedin_poster.py
import pyperclip
import pyautogui
import webbrowser
import time

def post_on_linkedin(message):
    webbrowser.open("https://www.linkedin.com/feed/")
    time.sleep(10)
    pyautogui.click(100, 250)  # Click 'Start a post' (may need to adjust coordinates)
    time.sleep(2)
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.press("tab", presses=3)
    pyautogui.press("enter")
    return "✅ LinkedIn post attempted (check browser window)."
