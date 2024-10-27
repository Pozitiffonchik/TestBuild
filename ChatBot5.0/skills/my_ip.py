
import requests

def handle_ip_query(query):
    try:
        # Using a public API to fetch IP
        response = requests.get("https://api.ipify.org?format=json")
        ip_data = response.json()
        return f"Your IP address is {ip_data['ip']}"
    except Exception as e:
        return f"Could not retrieve IP: {str(e)}"
