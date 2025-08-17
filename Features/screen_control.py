import pyautogui
import subprocess
import os
from TextToSpeach.Fast_DF_TTS import speak
import time

class ScreenController:
    def __init__(self):
        pyautogui.FAILSAFE = False
        self.screenshot_dir = "Data/Screenshots"
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def take_screenshot(self):
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            filepath = os.path.join(self.screenshot_dir, filename)
            
            screenshot = pyautogui.screenshot()
            screenshot.save(filepath)
            speak("Screenshot captured and saved")
            return True
        except Exception as e:
            print(f"Error taking screenshot: {e}")
            return False

    def start_screen_recording(self):
        try:
            import cv2
            import numpy as np
            from PIL import ImageGrab
            
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"recording_{timestamp}.avi"
            filepath = os.path.join(self.screenshot_dir, filename)
            
            speak("Starting screen recording. Say 'stop recording' to finish.")
            # Start recording code here
            
        except Exception as e:
            print(f"Error starting recording: {e}")

    def lock_screen(self):
        try:
            subprocess.run("rundll32.exe user32.dll,LockWorkStation", shell=True)
            speak("Screen locked")
        except Exception as e:
            print(f"Error locking screen: {e}") 