import psutil
import time
from datetime import datetime

def monitor_system(log_file):
    with open(log_file, "a") as f:
        while True:
            # Get the current time
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Get CPU percentage
            cpu_percent = psutil.cpu_percent(interval=1)

            # Write data to log file
            f.write(f"Time: {current_time}, CPU Usage: {cpu_percent}%\n")
            f.flush()  # Ensure the data is written to the file immediately

            # Sleep for 1 second before the next reading
            time.sleep(60)

if __name__ == "__main__":
    log_file = "system_monitor_log.txt"
    monitor_system(log_file)