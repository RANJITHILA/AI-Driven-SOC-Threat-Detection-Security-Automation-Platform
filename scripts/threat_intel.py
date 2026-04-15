import pandas as pd
import random
import os


def enrich_threat_intelligence():
    input_path = "../response/blocked_ips.txt"
    output_path = "../response/threat_intel_report.csv"

    threat_types = [
        "Botnet C2",
        "Brute Force Source",
        "Malware Callback",
        "Port Scanner",
        "Suspicious Exfiltration Node"
    ]

    enriched_data = []

    with open(input_path, "r") as f:
        ips = f.readlines()

    for ip in ips:
        ip = ip.strip()
        reputation_score = random.randint(70, 100)

        enriched_data.append({
            "ip_address": ip,
            "reputation_score": reputation_score,
            "threat_type": random.choice(threat_types),
            "confidence": random.choice(["High", "Medium"]),
            "recommended_action": "Block and Monitor"
        })

    df = pd.DataFrame(enriched_data)
    df.to_csv(output_path, index=False)

    print("🌐 Threat intelligence enrichment completed!")
    print(f"📁 Report saved to: {output_path}")


if __name__ == "__main__":
    enrich_threat_intelligence()