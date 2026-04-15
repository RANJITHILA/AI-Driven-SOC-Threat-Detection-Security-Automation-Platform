import pandas as pd
import os
import joblib
from sklearn.ensemble import IsolationForest


def train_threat_model():
    input_path = "../data/processed_logs.csv"
    model_path = "../models/threat_model.pkl"

    # Load processed data
    df = pd.read_csv(input_path)

    # Train Isolation Forest
    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    model.fit(df)

    # Predict anomalies for validation
    df["anomaly"] = model.predict(df)

    # Save model
    os.makedirs("../models", exist_ok=True)
    joblib.dump(model, model_path)

    # Save validation output
    df.to_csv("../data/model_output.csv", index=False)

    print("✅ AI Threat Detection Model trained successfully!")
    print(f"📁 Model saved to: {model_path}")
    print("🚨 -1 = Suspicious | 1 = Normal")


if __name__ == "__main__":
    train_threat_model()