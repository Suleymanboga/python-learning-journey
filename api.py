"""I learned about APIs in Python... I'm always continuing to learn."""
import requests

def ip_query():
    print("---  IP Address Intelligence Tool ---")
    ip_address = input("IP to be queried (Leave blank for your IP): ")
    url = f"http://ip-api.com/json/{ip_address}"
    answer = requests.get(url, timeout=10)
    data = answer.json()
    if data["status"] == "success":
        print("TARGET DETECTED!")
        print(f"Country: {data['country']}")
        print(f"City: {data['city']}")
        print(f"Internet Service Provider (ISP): {data['isp']}")
        print(f"Latitude/Longitude: {data['lat']}, {data['lon']}")
    else:
        print("Error: IP address not found!")
ip_query()
