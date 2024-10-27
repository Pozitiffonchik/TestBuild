from datetime import datetime

def handle_current_time_query(query):
    """Return the current time."""
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"The current time is {current_time}."
