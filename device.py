import socket
import platform
import json

# collection of system information
hostname = socket.gethostname()
hostos = platform.system()
hostosver = platform.version()

# dictionary of the data
device_info = {
    "device_name": hostname,
    "operating_system": hostos,
    "os_version": hostosver
}

with open("device_info.json", "w") as f:
    json.dump(device_info, f, indent=4)
