from pathlib import Path
import joblib
import pandas as pd

from app.ml.preprocess import prepare_dataframe


ARTIFACTS_DIR = Path(__file__).resolve().parent / "artifacts"


class ThreatPredictor:
    def __init__(self):
        self.model = joblib.load(ARTIFACTS_DIR / "threat_model.pkl")
        self.scaler = joblib.load(ARTIFACTS_DIR / "scaler.pkl")
        self.feature_columns = joblib.load(ARTIFACTS_DIR / "feature_columns.pkl")

    def predict_event(self, event: dict):
        df = pd.DataFrame([event])
        df = prepare_dataframe(df)

        X = df[self.feature_columns]
        X_scaled = self.scaler.transform(X)

        prediction = self.model.predict(X_scaled)[0]
        probability = self.model.predict_proba(X_scaled)[0][1]

        return {
            "prediction": "suspicious" if int(prediction) == 1 else "normal",
            "probability": round(float(probability), 4)
        }


if __name__ == "__main__":
    sample_event = {
        "failed_attempts": 7,
        "request_count": 120,
        "is_new_ip": 1,
        "is_new_device": 1,
        "location": "Unknown",
        "login_hour": 2
    }

    predictor = ThreatPredictor()
    result = predictor.predict_event(sample_event)
    print(result)