import random

question_responses = [
        "I'm doing great, thank you! How can I help you?",
        "I'm just a bot, but I'm here to help you!",
        "I’m doing well! What can I assist you with?",
        "I'm here and ready to assist you. How can I help?",
        "I'm functioning perfectly! How can I assist you?"
    ]

def handle_question_query(query):
    return random.choice(question_responses)