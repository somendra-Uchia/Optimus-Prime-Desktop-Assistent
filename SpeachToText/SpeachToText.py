#-------------------------------------ONLY LISTEN AND PRINT FUNCTION----------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from os import getcwd
import requests
from playsound import playsound  # pip install playsound==1.2.2
import os
from typing import Union  # pip install typing
import time
#Setting upb the Chrome Options with specific argument
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--headless=new")
#Setting up the Chrome driver with WebDriver and options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
website = "https://allorizenproject1.netlify.app/"
#Opening the website in chrome browser
driver.get(website)
Recog_File = f"{getcwd()}\\input.txt"

def listen():
    while True:
        try:
            start_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'startButton'))
            )
            start_button.click()
            print("Listening...")
            
            output_text = ""
            
            while True:
                output_element = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.ID, 'output'))
                )
                current_text = output_element.text.strip()
                
                if current_text and current_text != output_text:
                    output_text = current_text
                    # Write to input.txt with proper path
                    with open("input.txt", "w", encoding='utf-8') as file:
                        file.write(output_text.lower())
                    print("USER:", output_text)
                
                time.sleep(0.1)
                
        except Exception as e:
            print(f"Error in listen: {e}")
            time.sleep(1)


