import pygame
import os
import threading
from TextToSpeach.Fast_DF_TTS import speak

def stop_theme_song():
    try:
        pygame.mixer.music.stop()
        speak("Stopping theme song")
    except:
        pass

def play_theme_song():
    try:
        pygame.mixer.init()
        # Update this path to match your actual theme song location
        theme_path = os.path.join(os.path.dirname(__file__), 'Transformers Prime Opening.mp3')
        
        if os.path.exists(theme_path):
            speak("Playing Transformers theme song")
            pygame.mixer.music.load(theme_path)
            pygame.mixer.music.play()
    
            # Wait for the song to finish or stop command
            while pygame.mixer.music.get_busy():
                try:
                    with open("input.txt", "r") as file:
                        command = file.read().lower().strip()
                        if any(stop_cmd in command for stop_cmd in [
                            "stop theme song", 
                            "stop song", 
                            "stop music",
                            "band karo",
                            "music band karo",
                            "theme song band karo"
                        ]):
                            stop_theme_song()
                            break
                except:
                    pass
                pygame.time.Clock().tick(10)
        else:
            speak("Theme song file not found")
            print(f"Theme song not found at: {theme_path}")
    except Exception as e:
        print(f"Error playing theme song: {e}")