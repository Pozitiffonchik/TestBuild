import random

goodbye_responses = [
        "Goodbye! Have a great day!",
        "See you later! Take care!",
        "Talk to you later!",
        "Bye! Have a nice day!",
        "Goodbye! See you next time!"
    ]


def handle_goodbye_query(query):
    return random.choice(goodbye_responses)