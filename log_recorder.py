"""I learned about json files in Python... I'm always continuing to learn."""
import json


logs = [
    {
        "date": "2024-12-22",
        "event": "Unauthorized Access Attempt",
        "ip": "192.168.1.55",
        "status": "Blocked"
    },
    {
        "date": "2024-12-22",
        "event": "Data Leak",
        "ip": "10.0.0.2",
        "status": "Detected"
    }
]


print(" Saving data to 'logs.json'...")

with open("logs.json", "w", encoding="utf-8") as file:
    json.dump(logs, file, indent=4, ensure_ascii=False) 

print(" Save Successful!\n")


print(" Reading data from file...")

with open("logs.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)


for record in loaded_data:
    print(f"EVENT: {record['event']} | IP: {record['ip']}")
