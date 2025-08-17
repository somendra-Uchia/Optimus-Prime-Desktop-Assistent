from Automation.Automation_Brain import Auto_main_brain,clear_file
from SpeachToText.SpeachToText import listen
from TextToSpeach.Fast_DF_TTS import speak
import threading
from Data.DLG_Data import online_dlg,offline_dlg
import random
import time
from Time_Operations.brain import input_manage,input_manage_Alam
from Features.check_internet_speed import get_internet_speed
from Features.create_file import create_file
from Weather_Check.check_weather import get_weather_by_address
from Device_info.device_info import get_info
from Features.conversation import handle_conversation, ConversationHandler
from Features.play_theme import play_theme_song
from Whatsapp_automation.Whatsapp import send_whatsapp_message, send_whatsapp_file
from Features.self_learning import SelfLearningSystem
from datetime import datetime
import webbrowser
import os
from Features.system_control import SystemController
from Features.quick_notes import NotesManager
from Features.screen_control import ScreenController
from Features.task_manager import TaskManager


numbers = ["1:","2:","3:","4:","5:","6:","7:","8:","9:"]
spl_number = ["11:","12:"]

ran_online_dlg = random.choice(online_dlg)
ran_offnline_dlg = random.choice(offline_dlg)

# Initialize self-learning system
learning_system = SelfLearningSystem()

# Initialize new features
system_controller = SystemController()
notes_manager = NotesManager()
screen_controller = ScreenController()
task_manager = TaskManager()

def start_ui():
    try:
        # Get absolute path to UI file
        ui_path = os.path.join(os.getcwd(), 'UI', 'ui.htm')
        file_url = f'file:///{ui_path.replace(os.sep, "/")}'
        
        # Open in Chrome with normal window
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        if os.path.exists(chrome_path):
            # Open in a normal window with specific size
            os.system(f'start "" "{chrome_path}" --app={file_url} --window-size=800,600')
        else:
            webbrowser.open(file_url)
    except Exception as e:
        print(f"Error starting UI: {e}")

def minimize_ui():
    try:
        import win32gui
        import win32con
        # Find Chrome window with our UI
        def window_enum_handler(hwnd, windows):
            if "Chrome" in win32gui.GetWindowText(hwnd):
                win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        win32gui.EnumWindows(window_enum_handler, None)
    except:
        pass

def wait_for_input():
    """Helper function to wait for and return user input"""
    while True:
        try:
            with open("input.txt", "r") as file:
                text = file.read().strip()
            if text:
                return text
            time.sleep(0.1)
        except Exception as e:
            print(f"Error reading input file: {e}")
            time.sleep(0.1)

def check_inputs():
    output_text = ""
    handler = ConversationHandler()
    
    while True:
        try:
            with open("input.txt", "r") as file:
                input_text = file.read().lower().strip()
                
            if input_text and input_text != output_text:
                output_text = input_text
                print(f"Processing command: {output_text}")
                
                # Add exit commands
                if any(cmd in output_text for cmd in [
                    "you can sleep", "you can rest", 
                    "go to sleep", "take rest",
                    "shutdown", "turn off", 
                    "band ho jao", "so jao"
                ]):
                    speak("Thanks for using me sir. Have a great day!")
                    time.sleep(1)
                    os._exit(0)  # Clean exit
                    
                # Check for theme song commands
                if "play theme song" in output_text or "play your theme song" in output_text:
                    threading.Thread(target=play_theme_song).start()
                    clear_file()
                    continue
                elif any(stop_cmd in output_text for stop_cmd in [
                    "stop theme song", 
                    "stop song", 
                    "stop music",
                    "band karo",
                    "music band karo",
                    "theme song band karo"
                ]):
                    from Features.play_theme import stop_theme_song
                    stop_theme_song()
                    clear_file()
                    continue
                
                # First check for conversation commands
                if any(phrase in output_text for phrase in [
                    "introduce yourself", "who made you", "who are you",
                    "what is your mission", "who is your enemy"
                ]):
                    handle_conversation(output_text)
                    clear_file()
                    continue

                # Check for automation commands
                if output_text.startswith("open"):
                    Auto_main_brain(output_text)
                    clear_file()
                    continue
                    
                    
                # Check for other commands in Auto_main_brain
                if any(cmd in output_text for cmd in [
                    "search", "close", "check battery", 
                    "scroll", "pause", "stop"
                ]):
                    Auto_main_brain(output_text)
                    clear_file()
                    continue
                    
                # Handle schedule commands
                if output_text.startswith("tell me"):
                    output_text = output_text.replace(" p.m","PM").replace(" a.m","AM")
                    if "10:" in output_text or "11:" in output_text or "12:" in output_text:
                        input_manage(output_text)
                    else:
                        for number in numbers:
                            if number in output_text:
                                modified_text = output_text.replace(number, f"0{number}")
                                input_manage(modified_text)
                    clear_file()
                    continue

                # Handle alarm commands
                if output_text.startswith("set alarm"):
                    output_text = output_text.replace(" p.m","PM").replace(" a.m","AM")
                    if "10:" in output_text or "11:" in output_text or "12:" in output_text:
                        input_manage_Alam(output_text)
                    else:
                        for number in numbers:
                            if number in output_text:
                                modified_text = output_text.replace(number, f"0{number}")
                                input_manage_Alam(modified_text)
                    clear_file()
                    continue

                # Add scroll and click commands
                if any(cmd in output_text for cmd in [
                    "scroll", "click", "click here", "click on this",
                    "is video pe click karo", "is par click karo"
                ]):
                    from Automation.scroll_system import perform_scroll_action
                    perform_scroll_action(output_text)
                    clear_file()
                    continue

                # Process other commands...
                # (keep rest of your existing command checks)
                
                if "check internet speed" in output_text:
                    try:
                        speak("Sir Checking your internet speed")
                        speed = get_internet_speed()
                        speak(f"The device is running on {speed} Mega bytes per second")
                    except Exception as e:
                        speak("Sorry, I couldn't check the internet speed")
                        print(f"Error checking internet speed: {e}")
                    finally:
                        clear_file()

                if output_text.startswith("create"):
                    if "file" in output_text:
                        try:
                            create_file(output_text)
                        except Exception as e:
                            speak("Sorry, I couldn't create the file")
                            print(f"Error creating file: {e}")
                        finally:
                            clear_file()
                        
                if "check weather" in output_text or "weather in" in output_text:
                    try:
                        # Extract city name
                        text = output_text.replace("check weather in", "").replace("weather in", "").strip()
                        if text:
                            speak(f"Checking weather in {text}")
                            weather_info = get_weather_by_address(text)
                            speak(weather_info)
                        else:
                            speak("Please specify a city name")
                    except Exception as e:
                        speak("Sorry, I couldn't check the weather")
                        print(f"Error checking weather: {e}")
                    finally:
                        clear_file()
                    
                if "send whatsapp message" in output_text or "send message on whatsapp" in output_text:
                    try:
                        speak("To whom should I send the message?")
                        clear_file()
                        
                        contact_name = wait_for_input()
                        speak("What message should I send?")
                        clear_file()
                        
                        message = wait_for_input()
                        send_whatsapp_message(contact_name, message)
                    except Exception as e:
                        speak("Sorry, I couldn't send the WhatsApp message")
                        print(f"Error sending WhatsApp message: {e}")
                    finally:
                        clear_file()

                if "send whatsapp file" in output_text:
                    try:
                        speak("To whom should I send the file?")
                        clear_file()
                        
                        contact_name = wait_for_input()
                        speak("What's the file path?")
                        clear_file()
                        
                        file_path = wait_for_input()
                        send_whatsapp_file(contact_name, file_path)
                    except Exception as e:
                        speak("Sorry, I couldn't send the WhatsApp file")
                        print(f"Error sending WhatsApp file: {e}")
                    finally:
                        clear_file()
              
                
                # System control commands
                if any(cmd in output_text for cmd in ["volume", "brightness", "system info", "clean system"]):
                    if "volume" in output_text:
                        system_controller.adjust_volume(output_text)
                    elif "brightness" in output_text:
                        level = "medium"  # Default
                        if "low" in output_text: level = "low"
                        elif "high" in output_text: level = "high"
                        system_controller.adjust_brightness(level)
                    elif "system info" in output_text:
                        system_controller.get_system_info()
                    elif "clean system" in output_text:
                        system_controller.clean_system()
                    clear_file()
                    continue
                
                # Notes commands
                if "take note" in output_text or "make note" in output_text:
                    speak("What would you like me to note down?")
                    clear_file()
                    note_text = wait_for_input()
                    if note_text:
                        notes_manager.take_note(note_text)
                    clear_file()
                    continue
                if "read note" in output_text or "read latest note" in output_text:
                    notes_manager.read_latest_note()
                    clear_file()
                    continue
                
                # Screen control commands
                if any(cmd in output_text for cmd in ["screenshot", "screen recording", "lock screen"]):
                    if "screenshot" in output_text:
                        screen_controller.take_screenshot()
                    elif "screen recording" in output_text:
                        if "start" in output_text:
                            screen_controller.start_screen_recording()
                        elif "stop" in output_text:
                            screen_controller.stop_recording()
                    elif "lock screen" in output_text:
                        screen_controller.lock_screen()
                    clear_file()
                    continue
                
                # Task manager commands
                if any(cmd in output_text for cmd in ["running apps", "kill", "terminate", "monitor resources"]):
                    if "running apps" in output_text or "show running apps" in output_text:
                        task_manager.list_running_apps()
                    elif "kill" in output_text or "terminate" in output_text:
                        app = output_text.replace("kill", "").replace("terminate", "").strip()
                        task_manager.kill_app(app)
                    elif "monitor resources" in output_text:
                        task_manager.monitor_resources()
                    clear_file()
                    continue
                
            time.sleep(0.1)  # Prevent high CPU usage
                
        except Exception as e:
            # Get context for error recovery
            context = {
                "command": output_text,
                "time": str(datetime.now()),
                "file_path": "input.txt"  # Add relevant file paths
            }
            
            # Attempt recovery
            if not learning_system.log_error(e, context):
                speak("I encountered an error and couldn't recover automatically")
            
            clear_file()
            time.sleep(0.1)

def Optimus():
    try:
        clear_file()
        start_ui()  # Start UI first
        
        # Rest of your code remains exactly the same
        t1 = threading.Thread(target=listen, daemon=True)
        t2 = threading.Thread(target=check_inputs, daemon=True)
        t1.start() 
        t2.start()
        
        while True:
            time.sleep(0.1)
            
    except Exception as e:
        print(f"Error in Optimus: {e}")
