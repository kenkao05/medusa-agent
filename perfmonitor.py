import psutil
import time
import json

def collect_usage(prev_net):
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    new_net = psutil.net_io_counters()

    # calculates upload/download in KB/s
    sent_kb = (new_net.bytes_sent - prev_net.bytes_sent) / 1024
    recv_kb = (new_net.bytes_recv - prev_net.bytes_recv) / 1024

    usage = {
        "cpu_usage_percent": round(cpu, 2),
        "memory_usage_percent": round(mem, 2),
        "network_upload_kbps": round(sent_kb, 2),
        "network_download_kbps": round(recv_kb, 2)
    }

    return usage, new_net

# initial network snapshot
prev_net = psutil.net_io_counters()
output_file = "performance.json"

print("🔄 Logging system performance every 1 second... Press Ctrl+C to stop.")

try:
    while True:
        usage_data, prev_net = collect_usage(prev_net)

        # write current version to JSON
        with open(output_file, "w") as f:
            json.dump(usage_data, f, indent=4)

        time.sleep(1) # time it takes to reload

except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped by user.")

