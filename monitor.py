import psutil
import time
import logging
import smtplib
from email.mime.text import MIMEText

# --- CONFIGURATION ---
CPU_THRESHOLD = 80      # Alert if CPU > 80%
RAM_THRESHOLD = 80      # Alert if RAM > 80%
DISK_THRESHOLD = 90     # Alert if Disk > 90%
CHECK_INTERVAL = 60     # Check every 60 seconds
LOG_FILE = "server_health.log"

# --- LOGGING SETUP ---
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_alert(subject, body):
    """Simulates sending an email alert (Print to console for demo)"""
    # In a real enterprise script, you would use smtplib here to send real emails.
    alert_msg = f"*** ALERT TRIGGERED ***\nSubject: {subject}\nMessage: {body}\n"
    print(alert_msg)
    logging.warning(f"ALERT SENT: {subject}")

def check_system_health():
    # 1. Check CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        send_alert("High CPU Usage", f"CPU is at {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)")

    # 2. Check Memory (RAM)
    memory = psutil.virtual_memory()
    if memory.percent > RAM_THRESHOLD:
        send_alert("High Memory Usage", f"Memory is at {memory.percent}% (Threshold: {RAM_THRESHOLD}%)")

    # 3. Check Disk Space
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        send_alert("Low Disk Space", f"Disk usage is at {disk.percent}% (Threshold: {DISK_THRESHOLD}%)")

    # Log normal health check
    logging.info(f"Health Check: CPU {cpu_usage}% | RAM {memory.percent}% | Disk {disk.percent}%")

if __name__ == "__main__":
    print(f"Starting Server Monitor... (Logging to {LOG_FILE})")
    print("Press Ctrl+C to stop.")
    
    try:
        while True:
            check_system_health()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\nStopping monitor. Goodbye!")
