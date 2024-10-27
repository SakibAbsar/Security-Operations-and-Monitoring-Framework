
import time
import yaml

def load_monitor_config():
    with open("config/log_monitor_config.yaml", "r") as f:
        return yaml.safe_load(f)

def monitor_logs():
    config = load_monitor_config()
    for log_file in config["monitor_directories"]:
        with open(log_file, "r") as f:
            f.seek(0, 2)  # Move to end of file
            while True:
                line = f.readline()
                if not line:
                    time.sleep(1)
                    continue
                if any(keyword in line for keyword in config["alert_keywords"]):
                    print(f"Alert: {line.strip()}")

if __name__ == "__main__":
    monitor_logs()
