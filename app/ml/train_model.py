from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from app.ml.preprocess import split_and_scale, FEATURE_COLUMNS


BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "training_dataset.csv"
ARTIFACTS_DIR = Path(__file__).resolve().parent / "artifacts"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


def train():
    df = pd.read_csv(DATA_PATH)

    X_train, X_test, X_train_scaled, X_test_scaled, y_train, y_test, scaler = split_and_scale(df)

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced"
    )
    model.fit(X_train_scaled, y_train)

    joblib.dump(model, ARTIFACTS_DIR / "threat_model.pkl")
    joblib.dump(scaler, ARTIFACTS_DIR / "scaler.pkl")
    joblib.dump(FEATURE_COLUMNS, ARTIFACTS_DIR / "feature_columns.pkl")

    print("Model trained and artifacts saved successfully.")
    print(f"Saved to: {ARTIFACTS_DIR}")


if __name__ == "__main__":
    train()