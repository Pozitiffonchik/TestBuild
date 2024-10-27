import random

help_responses =[
        "I'm here to help you. What do you need assistance with?",
        "How can I assist you today?",
        "I'm ready to help. What do you need?",
        "Let me know how I can help you.",
        "I'm here to provide assistance. What do you need?"
    ]


def handle_help_query(query):
    return random.choice(help_responses)