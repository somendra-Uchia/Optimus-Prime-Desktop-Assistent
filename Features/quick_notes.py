import os
from datetime import datetime
from TextToSpeach.Fast_DF_TTS import speak

class NotesManager:
    def __init__(self):
        self.notes_dir = "Data/Notes"
        os.makedirs(self.notes_dir, exist_ok=True)

    def take_note(self, text):
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"note_{timestamp}.txt"
            filepath = os.path.join(self.notes_dir, filename)
            
            with open(filepath, "w") as f:
                f.write(text)
            
            speak("Note saved successfully")
            return True
        except Exception as e:
            print(f"Error saving note: {e}")
            return False

    def read_latest_note(self):
        try:
            notes = os.listdir(self.notes_dir)
            if notes:
                latest_note = max(notes, key=lambda x: os.path.getctime(os.path.join(self.notes_dir, x)))
                with open(os.path.join(self.notes_dir, latest_note), "r") as f:
                    content = f.read()
                speak("Your latest note says: " + content)
            else:
                speak("No notes found")
        except Exception as e:
            print(f"Error reading note: {e}") 