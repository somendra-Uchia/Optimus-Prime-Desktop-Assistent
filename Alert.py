import os
from winotify import Notification, audio
from os import getcwd

def Alert(Text):
    icon_path = r"C:\Users\Somendra\OneDrive\Desktop\OPTIMUS-PRIME\logo.jpeg"

    toast = Notification(
        app_id = " OPTIMUS-PRIME ",
        title = Text,
        duration = "long",
        icon = icon_path   
   )
    toast.set_audio(audio.Default, loop = False)


    toast.add_actions(label = "Click me" , launch = "https://www.google.com")
    toast.add_actions(label = "Dismiss" , launch = "https://www.google.com")

    toast.show()

