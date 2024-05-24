import webbrowser
import pyautogui
import time

from urllib.parse import quote

from script import Convert

def WhatsAppBot(phones, message):
  
  try:
    phones = phones.split()
    formated_phones = Convert.FORMAT_PHONE(phones)

    encoded_message = quote(message)

    screen_width, screen_height = pyautogui.size()

    for phone in formated_phones:
      webbrowser.open(f"https://web.whatsapp.com/send?phone={phone}&text={encoded_message}")

      time.sleep(10)
      pyautogui.click(screen_width / 2, screen_height / 2)
      pyautogui.press('enter')

      time.sleep(1.5)
      pyautogui.hotkey('ctrl', 'w')

    return 200
  except:
    return 500