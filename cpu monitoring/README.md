# CPU Monitoring Script (Windows & Linux)

This Python script monitors the **CPU usage** of your system at regular intervals.  
If the CPU usage **exceeds the defined threshold** (default: 80%), it will:  

- Show a **desktop notification** (Windows & Linux GUI).  
- Print an **alert message** in the terminal.  
- Write logs (with timestamp) to `cpu_monitor.log`.  

---

## Features
- Works on **both Windows and Linux**.  
- **Logging** of every CPU usage reading with timestamps.  
- **Alerts** when CPU usage exceeds the threshold.  
- Handles **headless Linux servers** (no GUI): falls back to console + log alerts.  
- Adjustable **threshold** and **interval**.  

---

## Additional Setup for Linux GUI

On Linux with GUI, plyer uses notify-send for notifications.
Make sure it is installed:

```bash
sudo apt-get install libnotify-bin




