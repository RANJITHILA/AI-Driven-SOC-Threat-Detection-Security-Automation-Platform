import re
from datetime import datetime


def auto_respond():
    alert_path = "../logs/alerts.log"
    blocked_path = "blocked_ips.txt"
    incident_path = "incidents.log"

    blocked_ips = set()

    with open(alert_path, "r") as f:
        alerts = f.readlines()

    with open(blocked_path, "w") as blocked_file, open(incident_path, "w") as incident_file:
        for alert in alerts:
            # Simulate suspicious IP extraction
            fake_ip = f"192.168.1.{len(blocked_ips)+100}"
            blocked_ips.add(fake_ip)

            # Write blocked IP
            blocked_file.write(f"{fake_ip}\n")

            # Write incident log
            incident_message = (
                f"[{datetime.now()}] INCIDENT CREATED | "
                f"Blocked IP={fake_ip} | "
                f"Reason=AI detected suspicious behavior\n"
            )
            incident_file.write(incident_message)

    print(f"⚡ {len(blocked_ips)} malicious IPs blocked!")
    print("📁 Incident response actions completed.")


if __name__ == "__main__":
    auto_respond()