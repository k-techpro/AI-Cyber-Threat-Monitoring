from app.services.ml_detector import predict_threat

def test_ml():
    sample = {
        "high_failed_attempts": 1,
        "high_request_count": 1,
        "is_new_ip": 1,
        "is_new_device": 1,
        "unknown_location": 1,
        "unusual_time": 1
    }

    result = predict_threat(sample)
    print(result)

if __name__ == "__main__":
    test_ml()