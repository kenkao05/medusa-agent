import psutil
import socket
import json

def get_open_ports():
    connections = psutil.net_connections(kind='inet')
    open_ports = []

    for conn in connections:
        if conn.status == psutil.CONN_LISTEN:
            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "?"
            pid = conn.pid
            try:
                process = psutil.Process(pid) if pid else None
                pname = process.name() if process else "System"
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pname = "Unknown"

            proto = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"

            open_ports.append({
                "Protocol": proto,
                "Address": laddr,
                "PID": pid,
                "Process": pname
            })

    return open_ports

def write_open_ports_to_json(filename="open_ports.json"):
    ports = get_open_ports()
    with open(filename, "w") as f:
        json.dump(ports, f, indent=4)
    print(f"✅ Open ports written to {filename}")

if __name__ == "__main__":
    write_open_ports_to_json()