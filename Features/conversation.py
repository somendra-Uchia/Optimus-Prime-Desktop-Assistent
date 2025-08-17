from difflib import get_close_matches
from TextToSpeach.Fast_DF_TTS import speak
import time
import json
import os
from SpeachToText.SpeachToText import listen
from Automation.Automation_Brain import clear_file

# Load existing questions
questions = {
    "introduce yourself": "I    am     Optimus Prime,     leader  of     the Autobots, We  are  an advanced  race of sentient  robotic beings from   Planet Cybertron,",
    "who made you": "i was created by the ancient cybertronian race known as the primes but i am currently forged in the form of a desktop assistant by Soommendra",
    "where are you from": "i am from the planet cybertron",
    "what is your mission": "to protect humanity and defeat the decepticons",
    "who is your enemy": "my greatest enemy is megatron the leader of the decepticons",
    "can you transform": "yes i can transform into a powerful truck",
    "who created you": "i was created by the ancient cybertronian race known as the primes",
    "what is the matrix of leadership": "the matrix of leadership is a powerful artifact that holds the wisdom of past leaders"

}

class ConversationHandler:
    def __init__(self):
        self.last_response_time = 0
        self.new_qa_file = "Data/new_questions.json"
        self.questions = self.load_all_questions()
        
    def load_all_questions(self):
        """Load both default and learned questions"""
        # Start with default questions
        questions = {
             "introduce yourself": "I    am     Optimus Prime,     leader  of     the Autobots, We  are  an advanced  race of sentient  robotic beings from   Planet Cybertron,",
            "who made you": "i was created by the ancient cybertronian race known as the primes but i am currently forged in the form of a desktop assistant by Soommendra",
            "where are you from": "i am from the planet cybertron",
            # ... (rest of your default questions)
        }
        
        # Load learned questions
        try:
            if os.path.exists(self.new_qa_file):
                with open(self.new_qa_file, 'r') as f:
                    learned_qa = json.load(f)
                    questions.update(learned_qa)
        except Exception as e:
            print(f"Error loading learned questions: {e}")
            
        return questions

    def save_new_question(self, question, answer):
        """Save new question-answer pair"""
        try:
            # Load existing learned questions
            learned_qa = {}
            if os.path.exists(self.new_qa_file):
                with open(self.new_qa_file, 'r') as f:
                    learned_qa = json.load(f)
            
            # Add new question
            learned_qa[question.lower()] = answer
            
            # Save updated questions
            with open(self.new_qa_file, 'w') as f:
                json.dump(learned_qa, f, indent=4)
            
            # Update current questions
            self.questions[question.lower()] = answer
            
            speak("Thank you for teaching me. I've learned something new.")
            return True
            
        except Exception as e:
            print(f"Error saving new question: {e}")
            return False

    def learn_new_answer(self, question):
        """Learn answer to unknown question"""
        try:
            speak("I don't know the answer to that question. Would you like to teach me?")
            clear_file()
            
            response = wait_for_input().lower()
            if "yes" in response or "sure" in response or "okay" in response:
                speak("Please tell me the answer.")
                clear_file()
                
                answer = wait_for_input()
                if answer:
                    if self.save_new_question(question, answer):
                        return answer
            else:
                speak("Alright, I'll try to learn this another time.")
                
        except Exception as e:
            print(f"Error learning new answer: {e}")
        return None

    def get_response(self, user_input):
        """Get response for user input"""
        try:
            user_input = user_input.lower().strip()
            
            # Direct match
            if user_input in self.questions:
                return self.questions[user_input]
            
            # Try fuzzy matching
            closest_matches = get_close_matches(user_input, list(self.questions.keys()), n=1, cutoff=0.7)
            if closest_matches:
                return self.questions[closest_matches[0]]
            
            # If no match found, try to learn
            return self.learn_new_answer(user_input)
            
        except Exception as e:
            print(f"Error in conversation: {e}")
            return None

def wait_for_input():
    """Wait for user input"""
    while True:
        try:
            with open("input.txt", "r") as file:
                text = file.read().strip()
            if text:
                return text
            time.sleep(0.1)
        except Exception as e:
            print(f"Error reading input: {e}")
            time.sleep(0.1)

def handle_conversation(text):
    """Main conversation handler"""
    if not text or not isinstance(text, str):
        return None
        
    handler = ConversationHandler()
    response = handler.get_response(text)
    
    if response:
        speak(response)
        return None
    
    return None