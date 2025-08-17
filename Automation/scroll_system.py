import pyautogui
import time

def scroll_up():
    pyautogui.scroll(300)  # Single scroll up

def scroll_down():
    pyautogui.scroll(-300)  # Single scroll down

def scroll_left():
    pyautogui.press('left')

def scroll_right():
    pyautogui.press('right')

def scroll_to_home():
    pyautogui.press('home')

def scroll_to_end():
    pyautogui.press('end')

def click_at_position():
    # Get current mouse position and click
    pyautogui.click()

def perform_scroll_action(text):
    if "scroll up" in text or "upar scroll karo" in text:
        scroll_up()
    elif "scroll down" in text or "neeche scroll karo" in text:
        scroll_down()
    elif "scroll left" in text or "left scroll karo" in text or "left" in text:
        scroll_left()
    elif "scroll right" in text or "right scroll karo" in text or "right" in text:
        scroll_right()
    elif "scroll home" in text or "home par le jao" in text or "upar le jao" in text:
        scroll_to_home()
    elif "scroll end" in text or "end par le jao" in text or "neeche le jao" in text:
        scroll_to_end()
    elif any(click_cmd in text for click_cmd in ["click", "click here", "click on this", "is video pe click karo", "is par click karo"]):
        click_at_position()
    else:
        pass
