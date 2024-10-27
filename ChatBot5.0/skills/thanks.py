import random

thanks_responses = [
        "You're welcome!",
        "No problem!",
        "My pleasure!",
        "You're welcome! Happy to help.",
        "Anytime!"
    ]

def handle_thanks_query(query):
    return random.choice(thanks_responses)