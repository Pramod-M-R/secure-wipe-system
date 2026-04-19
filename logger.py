from datetime import datetime
import os

def log_event(message):
    log_path = os.path.join(os.getcwd(), "logs.txt")

    with open(log_path, "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] {message}\n")

    print(f"📝 Logged: {message}")
    print(f"📂 Log file: {log_path}\n")