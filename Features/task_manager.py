import psutil
from TextToSpeach.Fast_DF_TTS import speak
import os

class TaskManager:
    def __init__(self):
        self.common_apps = {
            "chrome": "chrome.exe",
            "firefox": "firefox.exe",
            "word": "WINWORD.EXE",
            "excel": "EXCEL.EXE",
            "notepad": "notepad.exe",
            "explorer": "explorer.exe"
        }

    def list_running_apps(self):
        try:
            processes = []
            for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_percent']):
                if proc.info['cpu_percent'] > 0:  # Only show active processes
                    processes.append(proc.info)
            
            # Sort by CPU usage
            processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
            
            # Report top 5 processes
            speak("Top running applications are:")
            for proc in processes[:5]:
                speak(f"{proc['name']} using {proc['cpu_percent']:.1f}% CPU")
        except Exception as e:
            print(f"Error listing apps: {e}")

    def kill_app(self, app_name):
        try:
            app_name = app_name.lower()
            if app_name in self.common_apps:
                app_name = self.common_apps[app_name]
            
            killed = False
            for proc in psutil.process_iter():
                if proc.name().lower() == app_name.lower():
                    proc.kill()
                    killed = True
            
            if killed:
                speak(f"Terminated {app_name}")
            else:
                speak(f"Could not find {app_name}")
        except Exception as e:
            print(f"Error killing app: {e}")

    def monitor_resources(self):
        try:
            cpu = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            if cpu > 80:
                speak(f"Warning: High CPU usage at {cpu}%")
            if memory.percent > 80:
                speak(f"Warning: High memory usage at {memory.percent}%")
            if disk.percent > 90:
                speak(f"Warning: Low disk space, {disk.free // (2**30)} GB remaining")
        except Exception as e:
            print(f"Error monitoring resources: {e}") 