import os
import subprocess
import psutil
from TextToSpeach.Fast_DF_TTS import speak
import ctypes

class SystemController:
    def __init__(self):
        self.brightness_levels = {
            "low": 30,
            "medium": 50,
            "high": 100
        }

    def adjust_volume(self, command):
        try:
            from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, 0, None)
            volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
            
            if "mute" in command:
                volume.SetMute(1, None)
                speak("Audio muted")
            elif "unmute" in command:
                volume.SetMute(0, None)
                speak("Audio unmuted")
            elif "increase" in command:
                current_vol = volume.GetMasterVolumeLevelScalar()
                volume.SetMasterVolumeLevelScalar(min(1.0, current_vol + 0.1), None)
                speak("Volume increased")
            elif "decrease" in command:
                current_vol = volume.GetMasterVolumeLevelScalar()
                volume.SetMasterVolumeLevelScalar(max(0.0, current_vol - 0.1), None)
                speak("Volume decreased")
        except Exception as e:
            print(f"Error adjusting volume: {e}")

    def adjust_brightness(self, level):
        try:
            import screen_brightness_control as sbc
            if level in self.brightness_levels:
                sbc.set_brightness(self.brightness_levels[level])
                speak(f"Brightness set to {level}")
        except Exception as e:
            print(f"Error adjusting brightness: {e}")

    def get_system_info(self):
        try:
            cpu_usage = psutil.cpu_percent()
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            battery = psutil.sensors_battery()
            
            info = f"CPU Usage: {cpu_usage}%. "
            info += f"Memory Usage: {memory.percent}%. "
            info += f"Disk Usage: {disk.percent}%. "
            if battery:
                info += f"Battery: {battery.percent}%, "
                info += "Plugged In" if battery.power_plugged else "On Battery"
            
            speak(info)
        except Exception as e:
            print(f"Error getting system info: {e}")

    def clean_system(self):
        try:
            # Clear temp files
            temp = os.environ.get('TEMP')
            if temp:
                for file in os.listdir(temp):
                    try:
                        file_path = os.path.join(temp, file)
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                    except:
                        continue
            
            # Clear RAM
            subprocess.run("ipconfig /flushdns", shell=True)
            
            speak("System cleanup completed")
        except Exception as e:
            print(f"Error cleaning system: {e}") 