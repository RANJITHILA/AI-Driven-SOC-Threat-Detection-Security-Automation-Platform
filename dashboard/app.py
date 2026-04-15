from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Get project root path safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "response", "threat_intel_report.csv")


@app.route("/")
def dashboard():
    # Read threat intelligence report safely
    df = pd.read_csv(CSV_PATH)

    total_threats = len(df)
    avg_reputation = round(df["reputation_score"].mean(), 2)
    high_confidence = len(df[df["confidence"] == "High"])

    top_threats = df.head(10).to_dict(orient="records")

    return render_template(
        "index.html",
        total_threats=total_threats,
        avg_reputation=avg_reputation,
        high_confidence=high_confidence,
        top_threats=top_threats
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)