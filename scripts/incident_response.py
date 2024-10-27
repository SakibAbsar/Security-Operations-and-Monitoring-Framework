
import time

def initiate_incident_response(incident):
    print(f"Initiating response for: {incident}")
    if "SSH brute force" in incident:
        print("Blocking IP address...")
    elif "Suspicious outbound connection" in incident:
        print("Alerting network admin...")

def monitor_incidents():
    incidents = ["SSH brute force detected", "Suspicious outbound connection"]
    for incident in incidents:
        initiate_incident_response(incident)
        time.sleep(2)

if __name__ == "__main__":
    monitor_incidents()
