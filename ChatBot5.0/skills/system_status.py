import platform
import psutil

def handle_system_status_query(query):
    """Return the system status information."""
    uname = platform.uname()
    system_info = {
        "System": uname.system,
        #"Node Name": uname.node,
        #"Release": uname.release,
        "Version": uname.version,
        #"Machine": uname.machine,
        "Processor": uname.processor,
        "CPU Cores": psutil.cpu_count(logical=True),
        "Memory": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Used Memory": round(psutil.virtual_memory().used / (1024 ** 3), 2),
        "Free Memory": round(psutil.virtual_memory().free / (1024 ** 3), 2),
        "CPU Usage": psutil.cpu_percent(interval=1)
    }
    
    response = "\n".join([f"{key}: {value}" for key, value in system_info.items()])
    return f"System Status Information:\n{response}"
