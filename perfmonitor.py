import psutil
import time

def display_usage(cpu_usage, mem_usage, net_sent, net_recv, bars=30): 
    cpu_percent = cpu_usage / 100.0 # shows cpu and memory usage 
    mem_percent = mem_usage / 100.0

    mem_bar = '*' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))  #complicated math to make the |***----| thing
    cpu_bar = '*' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    print(
        f"CPU Usage: |{cpu_bar}| {cpu_usage:5.2f}%  "
        f"MEM Usage: |{mem_bar}| {mem_usage:5.2f}%  "
        f"⬇️ {net_recv:6.1f} KB/s  ⬆️ {net_sent:6.1f} KB/s",
        end="\r"
    )

old_net = psutil.net_io_counters() # first counters for calculating speed

while True:
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    new_net = psutil.net_io_counters() # second counters for calculating speed
    sent = (new_net.bytes_sent - old_net.bytes_sent) / 1024  # KB/s  Takes old bytes and subtracts from new to get total
    recv = (new_net.bytes_recv - old_net.bytes_recv) / 1024  # KB/s
    old_net = new_net

    display_usage(cpu, mem, sent, recv, 30)
    time.sleep(0.5)
