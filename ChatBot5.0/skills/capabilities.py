import random

capabilities_responses = [
        "I can help with various tasks such as answering questions, providing information, and more.",
        "I can assist you with answering questions, providing recommendations, and much more.",
        "I am here to help you with your queries and provide useful information.",
        "My capabilities include answering questions, providing information, and assisting with tasks.",
        "I can offer assistance with your questions and provide helpful information."
    ]

def handle_capabilities_query(query):
    return random.choice(capabilities_responses)