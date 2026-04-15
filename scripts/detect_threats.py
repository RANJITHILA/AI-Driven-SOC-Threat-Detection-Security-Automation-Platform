import pandas as pd
import joblib
from datetime import datetime


def detect_threats():
    model_path = "../models/threat_model.pkl"
    input_path = "../data/processed_logs.csv"
    alert_path = "../logs/alerts.log"

    # Load model
    model = joblib.load(model_path)

    # Load latest processed logs
    df = pd.read_csv(input_path)

    # Predict anomalies
    predictions = model.predict(df)

    # Add prediction column
    df["anomaly"] = predictions

    # Filter suspicious events
    threats = df[df["anomaly"] == -1]

    # Save alerts
    with open(alert_path, "w") as f:
        for index, row in threats.iterrows():
            alert_message = (
                f"[{datetime.now()}] HIGH ALERT: "
                f"Suspicious activity detected | "
                f"Port={row['port']} | "
                f"Bytes={row['bytes_transferred']} | "
                f"Failed_Login={row['failed_login']} | "
                f"Suspicious_Port={row['suspicious_port']}\n"
            )
            f.write(alert_message)

    print(f"🚨 {len(threats)} suspicious threats detected!")
    print(f"📁 Alerts saved to: {alert_path}")


if __name__ == "__main__":
    detect_threats()