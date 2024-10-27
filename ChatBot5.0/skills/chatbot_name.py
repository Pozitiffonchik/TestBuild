import random

name_responses = [
        "I'm your friendly chatbot Saya.",
        "You can call me Saya.!",
        "My name is Saya, your personal assistant.",
        "I am Saya, here to help you.",
        "I'm Saya, your friendly chatbot."
    ]

def handle_chatbot_name_query(query):
    return random.choice(name_responses)