import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


FEATURE_COLUMNS = [
    "failed_attempts",
    "request_count",
    "is_new_ip",
    "is_new_device",
    "unknown_location",
    "unusual_time",
    "high_failed_attempts",
    "high_request_count",
]


def prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["unknown_location"] = df["location"].astype(str).str.lower().eq("unknown").astype(int)
    df["unusual_time"] = ((df["login_hour"] < 6) | (df["login_hour"] > 22)).astype(int)
    df["high_failed_attempts"] = (df["failed_attempts"] >= 5).astype(int)
    df["high_request_count"] = (df["request_count"] >= 100).astype(int)

    return df


def split_and_scale(df: pd.DataFrame):
    df = prepare_dataframe(df)

    X = df[FEATURE_COLUMNS]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train, X_test, X_train_scaled, X_test_scaled, y_train, y_test, scaler