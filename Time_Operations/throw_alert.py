import os
import time
from Alert import Alert
from TextToSpeach.Fast_DF_TTS import speak
import threading
from Time_Operations.brain import input_manage
from os import getcwd


def load_schedule(file_path):    
    schedule = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    line_time, activity = line.strip().split(' = ')
                    schedule[line_time.strip()] = activity.strip()
    except Exception as e:
        print(f"Error loading schedule: {e}")
    return schedule

def check_schedule(file_path):   
    last_modified = 0
    alert_counts = {}
    last_alert_time = {}
    
    while True:
        try:
            current_time = time.strftime("%I:%M%p")
            schedule = load_schedule(file_path)
            
            if current_time in schedule:
                # Check if we haven't alerted too many times
                if alert_counts.get(current_time, 0) < 3:
                    # Check if enough time has passed since last alert
                    current_timestamp = time.time()
                    if current_time not in last_alert_time or current_timestamp - last_alert_time[current_time] >= 5:
                        text = schedule[current_time]
                        print(f"Schedule alert for {current_time}: {text}")
                        
                        # Show alert
                        Alert(text)
                        speak(text)
                        
                        # Update counters
                        alert_counts[current_time] = alert_counts.get(current_time, 0) + 1
                        last_alert_time[current_time] = current_timestamp
            
            time.sleep(1)  # Check every second
            
        except Exception as e:
            print(f"Error in check_schedule: {e}")
            time.sleep(1)

def load_AlamTime(file_path):   
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error loading alarm: {e}")
        return ""

def check_Alam(Alam_path):    
    last_modified = 0
    alarm_counts = {}
    last_alarm_time = {}
    
    while True:
        try:
            current_time = time.strftime("%I:%M%p")
            alarm_times = load_AlamTime(Alam_path)
            
            if current_time in alarm_times:
                # Check if we haven't alarmed too many times
                if alarm_counts.get(current_time, 0) < 3:
                    # Check if enough time has passed
                    current_timestamp = time.time()
                    if current_time not in last_alarm_time or current_timestamp - last_alarm_time[current_time] >= 5:
                        text = "Wake up! This is your alarm."
                        print(f"Alarm for {current_time}")
                        
                        # Show alarm
                        Alert(text)
                        speak(text)
                        
                        # Update counters
                        alarm_counts[current_time] = alarm_counts.get(current_time, 0) + 1
                        last_alarm_time[current_time] = current_timestamp
            
            time.sleep(1)
            
        except Exception as e:
            print(f"Error in check_Alam: {e}")
            time.sleep(1)
  

