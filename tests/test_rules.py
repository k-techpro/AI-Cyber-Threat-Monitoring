from app.core.security_rules import evaluate_security_rules

def test_rules():
    sample = {
        "failed_attempts": 7,
        "request_count": 120,
        "location": "Unknown",
        "login_hour": 2,
        "is_new_ip": 1,
        "is_new_device": 1
    }

    result = evaluate_security_rules(sample)
    print("Rules triggered:", result)

if __name__ == "__main__":
    test_rules()