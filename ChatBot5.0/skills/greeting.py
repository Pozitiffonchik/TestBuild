import random

# List of possible responses for greetings
greeting_responses = [
    "Hello! How can I assist you today?",
    "Hi there! What can I do for you?",
    "Good morning! How may I help you?",
    "Hello! How are you doing today?",
    "Hi! What can I help you with?"
]

# Function to handle greeting queries
def handle_greeting_query(query):
    return random.choice(greeting_responses)
