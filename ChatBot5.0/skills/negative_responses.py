import random

negative_responses = [
        "Alright, if you need anything else, just let me know.",
        "No problem. Let me know if you need anything.",
        "Okay, feel free to ask if you have any other questions.",
        "Understood. Let me know if there’s anything else.",
        "Got it. I'm here if you need anything."
    ]

def handle_negative_query(query):
    return random.choice(negative_responses)