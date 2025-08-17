import webbrowser
import pyautogui as ui
import time

def play_music_on_youtube(song_name, click_video=True):
    try:
        # Open YouTube and search for the song
        search_query = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"
        webbrowser.open(search_query)
        
        # Wait for the page to load
        time.sleep(4)
        
        # Use the tab key to navigate to the first video if click_video is True
        if click_video:
            ui.press('tab', presses=3, interval=0.2)  # Adjust the number of presses if needed
            time.sleep(0.2)
            ui.press('enter')  # Select the first video
            
    except Exception as e:
        print(f"Error playing music: {e}")

'''
# Uncomment this function to find the correct coordinates for your screen
def find_coordinates():
    print("Move mouse to first video position in 5 seconds...")
    time.sleep(5)
    x, y = ui.position()
    print(f"Mouse position: x={x}, y={y}")
'''








    
