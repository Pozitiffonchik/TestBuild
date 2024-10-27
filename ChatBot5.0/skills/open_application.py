# skills/open_application.py

import subprocess

def handle_open_application_query(query):
    """Open the specified application based on the query."""
    applications = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "command prompt": "cmd.exe",
    "chrome": "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "mozilla": "C:/Program Files/Mozilla Firefox/firefox.exe",
    "explorer": "explorer.exe",
    "tiger": "S:/TigerTrade.exe",
    "meta": "C:/Users/danri/AppData/Local/MetaScalp/MetaScalp.exe",
    "discord": "C:/Users/danri/AppData/Local/Discord/app-1.0.9168/Discord.exe",
    "telegram": "S:/Telegram Desktop/telegram.exe",
}



    query = " ".join(query.lower().strip().split()[1:])
    app_path = applications.get(query)
    
    if app_path:
        try:
            subprocess.Popen(app_path)
            return f"Opening {query.title()}..."
        except Exception as e:
            return f"Failed to open {query}. Error: {str(e)}"
    else:
        return f"Application '{query}' is not recognized."
