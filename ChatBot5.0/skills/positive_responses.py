import random

positive_responses = [
        "Great! How can I assist you?",
        "Awesome! What do you need help with?",
        "Fantastic! How can I help?",
        "Perfect! What can I do for you?",
        "Alright! How can I assist?"
    ]

def handle_positive_query(query):
    return random.choice(positive_responses)