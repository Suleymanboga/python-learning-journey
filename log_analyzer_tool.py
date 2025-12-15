"""Log Analyzer Tool v1.0
Scans list of logs for security threats using keyword matching."""
server_logs = [
    "INFO: User admin logged in successfully",
    "WARNING: High memory usage detected",
    "ERROR: Failed login attempt from IP 192.168.1.5",
    "INFO: User suleyman logged out",
    "ERROR: Failed login attempt from IP 10.0.0.2",
    "INFO: System update completed",
    "ERROR: Failed login attempt from IP 88.241.5.1",
    "WARNING: Disk space low"
]
failed_count = 0
for log in server_logs:
    if "failed" in log.lower():
        failed_count +=1
        print(f'THREAT DETECTED: {log}')

print("\n--- REPORT ---")
print(f"A total of {failed_count} failed login attempts were detected.")
if failed_count > 0:
    print("ALARM: SYSTEM UNDER ATTACK!")