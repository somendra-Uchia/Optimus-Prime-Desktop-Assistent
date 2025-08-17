import pyautogui

def open_new_tab():
    pyautogui.hotkey('ctrl', 't')

def close_tab():
    pyautogui.hotkey('ctrl', 'w')

def open_browser_menu():
    pyautogui.hotkey('alt', 'f')

def zoom_in():
    pyautogui.hotkey('ctrl', '+')

def zoom_out():
    pyautogui.hotkey('ctrl', '-')

def refresh_page():
    pyautogui.hotkey('ctrl', 'r')

def switch_to_next_tab():
    pyautogui.hotkey('ctrl', 'tab')

def switch_to_previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')

def open_history():
    pyautogui.hotkey('ctrl', 'h')

def open_bookmarks():
    pyautogui.hotkey('ctrl', 'b')

def go_back():
    pyautogui.hotkey('alt', 'left')

def go_forward():
    pyautogui.hotkey('alt', 'right')

def open_dev_tools():
    pyautogui.hotkey('ctrl', 'shift', 'i')

def toggle_full_screen():
    pyautogui.hotkey('f11')

def open_private_window():
    pyautogui.hotkey('ctrl', 'shift', 'n')

def perform_browser_action(command):
    command = command.lower()

    if 'new tab' in command or 'naya tab kholo' in command or 'open new tab' in command:
        open_new_tab()
    elif 'close tab' in command or 'tab band karo' in command or 'tab band kardo' in command:
        close_tab()
    elif 'menu' in command or 'open menue' in command:
        open_browser_menu()
    elif 'zoom in' in command or 'bada karo' in command or 'zoom karo' in command:
        zoom_in()
    elif 'zoom out' in command or 'chhota karo' in command or 'zoom out karo' in command:
        zoom_out()
    elif 'refresh' in command or 'reload' in command or 'page refresh karo' in command:
        refresh_page()
    elif 'next tab' in command or 'agla tab' in command or 'agla tab kholo' in command:
        switch_to_next_tab()
    elif 'previous tab' in command or 'pichla tab kholo' in command:
        switch_to_previous_tab()
    elif 'open history' in command or 'history kholo' in command:
        open_history()
    elif 'bookmarks' in command or 'bookmark kholo' in command:
        open_bookmarks()
    elif 'go back' in command or 'peeche jao' in command:
        go_back()
    elif 'go forward' in command or 'aage badho' in command:
        go_forward()
    elif 'dev tools' in command or 'developer tools' in command or 'developer tools kholo' in command:
        open_dev_tools()
    elif 'full screen' in command or 'poora screen' in command:
        toggle_full_screen()
    elif 'private window' in command or 'incognito' in command:
        open_private_window()
    else:
        pass


