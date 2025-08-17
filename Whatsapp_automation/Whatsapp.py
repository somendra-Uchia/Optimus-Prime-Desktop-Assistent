from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from TextToSpeach.Fast_DF_TTS import speak

class WhatsAppAutomation:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.setup_driver()

    def setup_driver(self):
        """Initialize the webdriver"""
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=./chrome-data')  # Save user data
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 20)
        
    def send_message(self, contact_name, message):
        """Send a message to a specific contact"""
        try:
            # Open WhatsApp Web
            self.driver.get("https://web.whatsapp.com/")
            speak("Please scan the QR code if needed")
            
            # Wait for the search box
            search_box = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            ))
            
            # Search for contact
            search_box.clear()
            search_box.send_keys(contact_name)
            time.sleep(2)  # Wait for search results
            
            # Click on the contact
            contact = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, f'//span[@title="{contact_name}"]')
            ))
            contact.click()
            
            # Find message box and send message
            message_box = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')
            ))
            message_box.send_keys(message)
            message_box.send_keys(Keys.ENTER)
            
            speak(f"Message sent to {contact_name}")
            return True
            
        except Exception as e:
            speak("Sorry, I couldn't send the message")
            print(f"Error sending message: {e}")
            return False

    def send_file(self, contact_name, file_path):
        """Send a file to a specific contact"""
        try:
            # Open WhatsApp Web
            self.driver.get("https://web.whatsapp.com/")
            speak("Please scan the QR code if needed")
            
            # Wait for the search box
            search_box = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            ))
            
            # Search for contact
            search_box.clear()
            search_box.send_keys(contact_name)
            time.sleep(2)
            
            # Click on the contact
            contact = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, f'//span[@title="{contact_name}"]')
            ))
            contact.click()
            
            # Click attachment button
            attachment = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//div[@title="Attach"]')
            ))
            attachment.click()
            
            # Find file input and send file
            file_input = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//input[@type="file"]')
            ))
            file_input.send_keys(file_path)
            
            # Wait and click send
            send_button = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, '//span[@data-icon="send"]')
            ))
            send_button.click()
            
            speak(f"File sent to {contact_name}")
            return True
            
        except Exception as e:
            speak("Sorry, I couldn't send the file")
            print(f"Error sending file: {e}")
            return False

    def close(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()

def send_whatsapp_message(contact, message):
    """Helper function to send WhatsApp message"""
    whatsapp = WhatsAppAutomation()
    try:
        success = whatsapp.send_message(contact, message)
        return success
    finally:
        whatsapp.close()

def send_whatsapp_file(contact, file_path):
    """Helper function to send WhatsApp file"""
    whatsapp = WhatsAppAutomation()
    try:
        success = whatsapp.send_file(contact, file_path)
        return success
    finally:
        whatsapp.close()
