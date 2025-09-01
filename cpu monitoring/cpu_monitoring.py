import psutil
from plyer import notification # type: ignore
import time
import logging
from datetime import datetime

# CPU usage threshold
THRESHOLD = 80
CHECK_INTERVAL = 60  # seconds

# Log file setup
LOG_FILE = "cpu_monitor.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def send_alert(usage):
    """Send a notification when CPU crosses threshold"""
    notification.notify(
        title="High CPU Usage Alert",
        message=f"CPU usage is {usage}%",
        timeout=5
    )


def monitor_cpu():
    print(f"Starting CPU monitoring...\nThreshold = {THRESHOLD}% | Interval = {CHECK_INTERVAL} sec")
    logging.info("CPU monitoring started.")

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)                  # measure CPU usage over 1 sec
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Log every reading
            logging.info(f"CPU usage: {cpu_usage}%")
            print(f"[{timestamp}] CPU usage: {cpu_usage}%")

            # Alert if threshold exceeded
            if cpu_usage > THRESHOLD:
                alert_msg = f"ALERT: CPU usage exceeded! CPU usage = {cpu_usage}%"
                print(alert_msg)
                logging.warning(alert_msg) 
                send_alert(cpu_usage)

            # Wait for remaining interval
            if CHECK_INTERVAL > 1:
                time.sleep(CHECK_INTERVAL - 1)      

    except KeyboardInterrupt:
        print("\nCPU monitoring stopped by user.")
        logging.info("CPU monitoring stopped by user.")


if __name__ == "__main__":
    monitor_cpu()
