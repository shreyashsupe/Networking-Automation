import psutil
from plyer import notification
import time

# CPU usage threshold
THRESHOLD = 80       
INTERVAL = 60        # seconds


def send_alert(usage):
    notification.notify(
        title = "High CPU usage Alert",
        message = "CPU usage is {cpu_usage}",
        # notification display time
        timeout = 5
    )
    


def monitor_cpu():
    print(f"Starting CPU monitoring .... \nThreshold = {THRESHOLD}% Interval = {INTERVAL} sec ")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)     # measure CPU usage over 1 sec
            print(f"CPU  usage: {cpu_usage}")

            if cpu_usage > THRESHOLD:
                print(f"Alert: CPU usage exceeded: CPU usage {cpu_usage}%")
                send_alert(cpu_usage)

            # wait for remianing interval
            if INTERVAL > 1:
                time.sleep(INTERVAL - 1)
            

    except KeyboardInterrupt:
        print("\nCPU monitoring stop by user")


if __name__ == "__main__":
    monitor_cpu()
