import pandas as pd
import random
from datetime import datetime, timedelta
import os


# -----------------------------
# Helper functions
# -----------------------------
def generate_ip():
    return f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"


def generate_log_entry():
    event_types = [
        "LOGIN_SUCCESS",
        "LOGIN_FAILED",
        "PORT_SCAN",
        "MALWARE_TRAFFIC",
        "NORMAL_BROWSING",
        "DATA_EXFILTRATION"
    ]

    event = random.choice(event_types)

    source_ip = generate_ip()
    destination_ip = generate_ip()

    port_mapping = {
        "LOGIN_SUCCESS": 22,
        "LOGIN_FAILED": 22,
        "PORT_SCAN": random.randint(1, 1024),
        "MALWARE_TRAFFIC": 4444,
        "NORMAL_BROWSING": random.choice([80, 443]),
        "DATA_EXFILTRATION": 443
    }

    protocol_mapping = {
        "LOGIN_SUCCESS": "TCP",
        "LOGIN_FAILED": "TCP",
        "PORT_SCAN": "TCP",
        "MALWARE_TRAFFIC": "TCP",
        "NORMAL_BROWSING": "HTTPS",
        "DATA_EXFILTRATION": "HTTPS"
    }

    bytes_mapping = {
        "LOGIN_SUCCESS": random.randint(500, 2000),
        "LOGIN_FAILED": random.randint(100, 500),
        "PORT_SCAN": random.randint(50, 150),
        "MALWARE_TRAFFIC": random.randint(1000, 5000),
        "NORMAL_BROWSING": random.randint(2000, 10000),
        "DATA_EXFILTRATION": random.randint(50000, 100000)
    }

    timestamp = datetime.now() - timedelta(minutes=random.randint(0, 1440))

    return {
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "port": port_mapping[event],
        "protocol": protocol_mapping[event],
        "bytes_transferred": bytes_mapping[event],
        "event_type": event
    }


# -----------------------------
# Main log generation
# -----------------------------
def generate_logs(num_logs=1000):
    logs = [generate_log_entry() for _ in range(num_logs)]
    df = pd.DataFrame(logs)

    os.makedirs("../logs", exist_ok=True)
    output_path = "../logs/network_logs.csv"
    df.to_csv(output_path, index=False)

    print(f"✅ {num_logs} logs generated successfully!")
    print(f"📁 Saved to: {output_path}")


if __name__ == "__main__":
    generate_logs()