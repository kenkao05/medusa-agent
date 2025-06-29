import socket
import platform

hostname = socket.gethostname()

hostos = platform.system()
hostosver = platform.version()

print(f"Device Name : {hostname}")
print(f"Device Name : {hostos}")
print(f"Device Name : {hostosver}")
