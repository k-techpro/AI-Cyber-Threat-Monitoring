from pathlib import Path
import joblib
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from app.ml.preprocess import split_and_scale


BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "training_dataset.csv"
ARTIFACTS_DIR = Path(__file__).resolve().parent / "artifacts"


def evaluate():
    df = pd.read_csv(DATA_PATH)

    X_train, X_test, X_train_scaled, X_test_scaled, y_train, y_test, scaler = split_and_scale(df)

    model = joblib.load(ARTIFACTS_DIR / "threat_model.pkl")

    y_pred = model.predict(X_test_scaled)

    print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    evaluate()