import pandas as pd
import os


def preprocess_logs():
    input_path = "../logs/network_logs.csv"
    output_path = "../data/processed_logs.csv"

    # Read raw logs
    df = pd.read_csv(input_path)

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Extract hour
    df["hour"] = df["timestamp"].dt.hour

    # Feature 1: failed login
    df["failed_login"] = df["event_type"].apply(
        lambda x: 1 if x == "LOGIN_FAILED" else 0
    )

    # Feature 2: suspicious port
    suspicious_ports = [4444, 3389, 445]
    df["suspicious_port"] = df["port"].apply(
        lambda x: 1 if x in suspicious_ports else 0
    )

    # Feature 3: high data transfer
    df["high_data_transfer"] = df["bytes_transferred"].apply(
        lambda x: 1 if x > 40000 else 0
    )

    # Encode event types
    df["event_code"] = df["event_type"].astype("category").cat.codes

    # Select ML-ready columns
    processed_df = df[
        [
            "port",
            "bytes_transferred",
            "hour",
            "failed_login",
            "suspicious_port",
            "high_data_transfer",
            "event_code"
        ]
    ]

    os.makedirs("../data", exist_ok=True)
    processed_df.to_csv(output_path, index=False)

    print("✅ Log preprocessing completed successfully!")
    print(f"📁 Saved to: {output_path}")


if __name__ == "__main__":
    preprocess_logs()   