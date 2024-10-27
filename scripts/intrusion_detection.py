
import re
import yaml

def load_ids_rules():
    with open("config/ids_rules.yaml", "r") as f:
        return yaml.safe_load(f)["rules"]

def detect_intrusion(log_file):
    rules = load_ids_rules()
    with open(log_file, "r") as f:
        for line in f:
            for rule in rules:
                if re.search(rule["pattern"], line):
                    print(f"Alert: {rule['description']} detected - {line.strip()}")

if __name__ == "__main__":
    detect_intrusion("/var/log/auth.log")
