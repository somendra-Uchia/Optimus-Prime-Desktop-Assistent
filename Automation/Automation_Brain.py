from TextToSpeach import Fast_DF_TTS
from Automation.Web_Open import openweb
from Automation.open_App import open_App
import pyautogui as gui
from Automation.Battery import check_percentage
from os import getcwd
import time
from Automation.tab_automation import perform_browser_action
from Automation.youtube_playback import perform_youtube_action
from Automation.scroll_system import perform_scroll_action
import threading
from TextToSpeach.Fast_DF_TTS import speak
import webbrowser
from Automation.Play_Music_YT import play_music_on_youtube

def play_pause():
    gui.press("space")
    
def search_google(text):
    webbrowser.open(f"https://www.google.com/search?q={text}")

def close():
    gui.hotkey('alt','f4')

def search(text):
    gui.press("/")
    time.sleep(0.3)
    gui.write(text)
    
def Open_Brain(text):
    if "website" in text or "open website named" in text:
        text = text.replace("open","").strip()
        text = text.replace("website","").strip()
        text = text.replace("open website named","").strip()
        t1 = threading.Thread(target=speak, args=(f"Navigating {text} website Sir",))
        t2 = threading.Thread(target=openweb, args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    else:
        text = text.replace("open","").strip()
        text = text.replace("app","").strip()
        t1 = threading.Thread(target=speak, args=(f"Navigating {text} application Sir",))
        t2 = threading.Thread(target=open_App, args=(text,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

def clear_file():
    with open(f"{getcwd()}\\input.txt","w") as file:
        file.truncate(0)        

def Auto_main_brain(text):
    try:
        if text.startswith("open"):
            Open_Brain(text)
            clear_file()
            
        elif "close" in text:
            close()
            clear_file()
            
        elif "play music" in text or "play music on youtube" in text:
            speak("Which song do you want to play sir?")
            clear_file()
            time.sleep(1)  # Wait for speech to complete
            
            # Wait for song name
            start_time = time.time()
            last_input = ""
            while time.time() - start_time < 15:  # 15 second timeout
                try:
                    with open("input.txt", "r") as file:
                        current_input = file.read().lower().strip()
                        
                        # Only process if input has changed and isn't empty
                        if current_input and current_input != last_input and current_input != "play music":
                            last_input = current_input
                            if "which song" not in current_input:
                                speak(f"Playing {current_input}")
                                play_music_on_youtube(current_input)
                                break
                except:
                    pass
                time.sleep(0.1)
            clear_file()
            
        elif text.startswith("play"):
            song_name = text.replace("play", "", 1).strip()
            if song_name:
                speak(f"Playing {song_name}")
                play_music_on_youtube(song_name, click_video=True)
            clear_file()
            
        elif "search" in text and "youtube" in text:
            query = text.replace("search", "").replace("on youtube", "").replace("for", "").strip()
            if query:
                speak(f"Searching for {query} on YouTube")
                play_music_on_youtube(query, click_video=False)
            clear_file()
            
        elif any(phrase in text for phrase in ["check battery percentage", "check battery level"]):
            check_percentage()
            clear_file()
            
        elif text.startswith("search"):
            text = text.replace("search","").strip()
            speak(f"Searching for {text} Sir")
            search(text)
            time.sleep(0.5)
            gui.press("enter")
            clear_file()
            
        else:
            # Try other actions
            perform_browser_action(text)
            perform_youtube_action(text)
            perform_scroll_action(text)
            clear_file()
            
    except Exception as e:
        print(f"Error in Auto_main_brain: {e}")
        clear_file()




