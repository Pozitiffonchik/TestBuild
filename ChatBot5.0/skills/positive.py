import random

positive_responses = [
        "I'm glad to hear that!",
        "That's wonderful!",
        "I'm happy you think so!",
        "That’s fantastic!",
        "Great to hear!"
    ]

def handle_positive_query(query):
    return random.choice(positive_responses)