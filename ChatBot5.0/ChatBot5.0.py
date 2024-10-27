import os
import json
import random
import importlib
import speech_recognition as sr
import pyttsx3
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline

nltk.download('punkt')

engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Female voice (1)

skill_handlers = {
    'math': 'handle_math_query',
    'my_ip': 'handle_ip_query',
    'current_time': 'handle_current_time_query',
    'system_status': 'handle_system_status_query',
    'open_application': 'handle_open_application_query',
}
def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def load_skill(skill_name, query):
    """Dynamically load a skill module and call its function."""
    try:
        skill_module = importlib.import_module(f'skills.{skill_name}')
        handler_name = skill_handlers.get(skill_name)
        
        if handler_name:
            skill_function = getattr(skill_module, handler_name, None)
            if skill_function:
                return skill_function(query)
            else:
                return f"The skill '{skill_name}' does not have an appropriate entry function."
        else:
            return f"Skill '{skill_name}' is not recognized."
    
    except ModuleNotFoundError:
        return f"Skill '{skill_name}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"


def listen_for_commands():
    """Listen for audio input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening for commands...")
        audio = recognizer.listen(source)
    
    try:
        voice = recognizer.recognize_google(audio)
        print("You:", voice)
        return voice.lower()
    except (sr.UnknownValueError, sr.RequestError) as e:
        print(f"Error recognizing audio: {e}")
        return ""


def load_json_file(file_path):
    """Load JSON data from a specified file path."""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []
    
    with open(file_path, 'r') as file:
        return json.load(file)


def load_training_data(file_path):
    """Load training data from JSON format."""
    data = load_json_file(file_path)
    return [(example['text'], label) for label, examples in data.items() for example in examples]


def load_responses(file_path):
    """Load response templates from JSON format."""
    return load_json_file(file_path)


class SKLearnClassifier:
    """Classifier for intent recognition using SKLearn."""
    def __init__(self):
        self.pipeline = make_pipeline(TfidfVectorizer(), SVC(kernel='linear'))

    def train(self, data):
        """Train the classifier using the provided data."""
        texts, labels = zip(*data)
        self.pipeline.fit(texts, labels)

    def predict(self, input_text):
        """Predict the intent of the input text."""
        return self.pipeline.predict([input_text])[0]

class ChatBot:
    """Main ChatBot class for handling user interactions."""
    def __init__(self, training_data_path, responses_path):
        self.model = SKLearnClassifier()
        self.responses = load_responses(responses_path)
        self.train(training_data_path)

    def train(self, training_data_path):
        """Train the ChatBot's model using training data."""
        data = load_training_data(training_data_path)
        self.model.train(data)

    def respond(self, input_text):
        """Generate a response based on the user's input."""
        intent = self.model.predict(input_text)
        response = load_skill(intent, input_text) if intent in ["math", "my_ip", "current_time", "system_status", "open_application"] else random.choice(self.responses.get(intent, ["I'm sorry, I don't understand what you want."]))
        return response

# Define file paths for training data and responses
training_data_path = 'S:/SayaAI/MyCode/ChatBot5.0/training_data/training_data5.0.json'
responses_path = 'S:/SayaAI/MyCode/ChatBot5.0/responses/responses5.0.json'

chatbot = ChatBot(training_data_path, responses_path)

print("ChatBot is now running. Say 'Exit' to stop.")
while True:
    user_input = listen_for_commands()
    
    if user_input and 'exit' in user_input:
        print("ChatBot: Goodbye!")
        speak("Goodbye!")
        break

    response = chatbot.respond(user_input)
    print(f"ChatBot: {response}")
    speak(response)
