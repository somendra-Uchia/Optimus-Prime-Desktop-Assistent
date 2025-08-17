import pyautogui

def volume_up():
    pyautogui.press('up')

def volume_down():
    pyautogui.press('down')

def seek_forward():
    pyautogui.press('right')

def seek_backward():
    pyautogui.press('left')

def seek_forward_10s():
    pyautogui.press('l')

def seek_backward_10s():
    pyautogui.press('j')

def seek_backward_frame():
    pyautogui.press(',')

def seek_forward_frame():
    pyautogui.press('.')

def seek_to_beginning():
    pyautogui.press('home')

def seek_to_end():
    pyautogui.press('end')

def seek_to_previous_chapter():
    pyautogui.hotkey('ctrl', 'left')

def seek_to_next_chapter():
    pyautogui.hotkey('ctrl', 'right')

def decrease_playback_speed():
    pyautogui.hotkey('shift', ',')

def increase_playback_speed():
    pyautogui.hotkey('shift', '.')

def move_to_next_video():
    pyautogui.hotkey('shift', 'n')

def move_to_previous_video():
    pyautogui.hotkey('shift', 'p')


def perform_youtube_action(command):
    if 'awaz tez karo' in command or 'up' in command or 'avaz bhadao' in command:
        volume_up()
    elif 'awaz kam karo' in command or 'down' in command or 'avaz ghatayo' in command:
        volume_down()
    elif 'aage badho' in command or 'right' in command:
        seek_forward()
    elif 'peeche jao' in command or 'left' in command:
        seek_backward()
    elif '10 second aage' in command or 'l' in command:
        seek_forward_10s()
    elif '10 second peeche' in command or 'j' in command:
        seek_backward_10s()
    elif 'frame peeche' in command or ',' in command:
        seek_backward_frame()
    elif 'frame aage' in command or '.' in command:
        seek_forward_frame()
    elif 'shuru se chalu karo' in command or 'beginning' in command or 'play from beginning' in command:
        seek_to_beginning()
    elif 'khatam par le jao' in command or 'end' in command:
        seek_to_end()
    elif 'pehla chapter' in command or 'previous chapter' in command:
        seek_to_previous_chapter()
    elif 'agla chapter' in command or 'next chapter' in command:
        seek_to_next_chapter()
    elif 'speed kam karo' in command or 'decrease speed' in command:
        decrease_playback_speed()
    elif 'speed badhao' in command or 'increase speed' in command:
        increase_playback_speed()
    elif 'agli video' in command or 'play next video' in command:
        move_to_next_video()
    elif 'pichli video' in command or 'previous video' in command or 'pehle vali video' in command:
        move_to_previous_video()
    else:
        pass


