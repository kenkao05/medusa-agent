import psutil
import socket

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

def print_open_ports():
    ports = get_open_ports()
    if not ports:
        print("🔒 No open ports found.")
        return

    print(f"{'Protocol':<6} {'Address':<22} {'PID':<6} Process")
    print("-" * 50)
    for port in ports:
        print(f"{port['Protocol']:<6} {port['Address']:<22} {str(port['PID']):<6} {port['Process']}")

if __name__ == "__main__":
    print_open_ports()
