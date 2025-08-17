import threading
from internet_check import is_Online
from Alert import Alert
from Data.DLG_Data import online_dlg,offline_dlg
import random
from co_brain import Optimus
from TextToSpeach.Fast_DF_TTS import speak
from Automation.Battery import check_plug
from Time_Operations.throw_alert import check_schedule,check_Alam
import time
import os

Alam_path = r'C:\Users\Somendra\OneDrive\Desktop\OPTIMUS-PRIME\Alam_data.txt'
file_path = r'C:\Users\Somendra\OneDrive\Desktop\OPTIMUS-PRIME\schedule.txt'

ran_online_dlg = random.choice(online_dlg)
ran_offnline_dlg = random.choice(offline_dlg)

def wish():
        t1 = threading.Thread(target = speak,args=(ran_online_dlg,))
        t2 = threading.Thread(target = Alert,args = (ran_online_dlg,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()

def main():
    if is_Online():
        wish()
        
        # Create daemon threads
        threads = [
            threading.Thread(target=check_plug, daemon=True),
            threading.Thread(target=check_schedule, args=(file_path,), daemon=True),
            threading.Thread(target=Optimus, daemon=True),
            threading.Thread(target=check_Alam, args=(Alam_path,), daemon=True)
        ]
        
        # Start all threads
        for thread in threads:
            thread.start()
            
        # Keep main thread alive
        try:
            while True:
                time.sleep(0.1)
        except (KeyboardInterrupt, SystemExit):
            print("\nShutting down gracefully...")
            speak("Thankyou kind sir. Have a great day!")
            time.sleep(1)
            os._exit(0)
    else:
        Alert(ran_offnline_dlg)

if __name__ == "__main__":
    main()

