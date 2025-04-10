import psutil
import time
import logging
from datetime import datetime


logging.basicConfig(filename='system_monitor.log', level=logging.INFO)

def monitor_system():
    Loops = 0
    while Loops < 1:
        Loops += 1
        print("-" * 50)

        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f" Time: {datetime.now()}")
        print(datetime.now())

        # CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")
        logging.info(f"CPU Usage: {cpu_usage}%")

        # Memory usage
        memory = psutil.virtual_memory()
        print(f"Memory Usage: {memory.percent}%")
        logging.info(f"Memory Usage: {memory.percent}%")

        # Disk usage
        disk_usage = psutil.disk_usage('/')
        print(f"Disk Usage: {disk_usage.percent} %")
        print(f"Disk Usage free: {disk_usage.free/1000000000} GB")
        print(f"Disk Usage used: {disk_usage.used/1000000000} GB")

        logging.info(f"Disk Usage: {disk_usage.percent}%")
        logging.info(f"Disk free: {disk_usage.free/1000000000} GB")
        logging.info(f"Disk used: {disk_usage.used/1000000000} GB")

        # Network usage
        network = psutil.net_io_counters()
        print(f"Bytes Sent: {network.bytes_sent}, Bytes Received: {network.bytes_recv}")
        logging.info(f"Bytes Sent: {network.bytes_sent}, Bytes Received: {network.bytes_recv}")

        # Adding a separator for readability
        print("-" * 50)

        # Wait for a few seconds before the next update
        # time.sleep(5)
if __name__ == '__main__':
    monitor_system()