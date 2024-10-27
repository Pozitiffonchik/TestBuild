import random

negative_responses = [
        "I'm sorry to hear that. Is there anything I can do to help?",
        "I’m here if you need to talk. How can I assist?",
        "I'm sorry you're feeling this way. How can I help?",
        "I’m sorry to hear that. Let me know if there's anything I can do.",
        "That sounds tough. How can I help?"
    ]

def handle_negative_query(query):
    return random.choice(negative_responses)