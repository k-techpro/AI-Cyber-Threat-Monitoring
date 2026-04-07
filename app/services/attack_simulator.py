import random
from datetime import datetime


USERNAMES = ["admin", "john", "divya", "guest", "manager", "analyst"]
LOCATIONS = ["Chennai", "Bangalore", "Mumbai", "Delhi", "Unknown", "Singapore"]
DEVICES = ["Windows Laptop", "Linux PC", "MacBook", "Android Phone", "iPhone"]
BROWSERS = ["Chrome", "Firefox", "Edge", "Safari"]
NORMAL_IPS = ["192.168.1.10", "192.168.1.20", "10.0.0.5", "172.16.0.11"]
ATTACK_IPS = ["45.67.210.11", "185.44.21.90", "103.88.122.5", "66.10.10.10"]


def _base_event():
    now = datetime.now()
    return {
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "login_hour": now.hour
    }


def generate_normal_event():
    event = _base_event()
    event.update({
        "username": random.choice(USERNAMES),
        "ip_address": random.choice(NORMAL_IPS),
        "location": random.choice(["Chennai", "Bangalore", "Mumbai"]),
        "device_type": random.choice(DEVICES),
        "browser": random.choice(BROWSERS),
        "status": random.choice(["SUCCESS", "SUCCESS", "FAILED"]),
        "failed_attempts": random.randint(0, 2),
        "request_count": random.randint(1, 20),
        "event_type": "normal_login",
        "is_new_ip": random.choice([0, 0, 1]),
        "is_new_device": random.choice([0, 0, 1]),
    })
    return event


def generate_bruteforce_event():
    event = _base_event()
    event.update({
        "username": random.choice(["admin", "manager", "guest"]),
        "ip_address": random.choice(ATTACK_IPS),
        "location": "Unknown",
        "device_type": random.choice(DEVICES),
        "browser": random.choice(BROWSERS),
        "status": "FAILED",
        "failed_attempts": random.randint(5, 10),
        "request_count": random.randint(40, 120),
        "event_type": "brute_force",
        "is_new_ip": 1,
        "is_new_device": random.choice([0, 1]),
    })
    return event


def generate_suspicious_login_event():
    event = _base_event()
    event.update({
        "username": random.choice(USERNAMES),
        "ip_address": random.choice(ATTACK_IPS),
        "location": random.choice(["Unknown", "Singapore"]),
        "device_type": random.choice(DEVICES),
        "browser": random.choice(BROWSERS),
        "status": "SUCCESS",
        "failed_attempts": random.randint(0, 1),
        "request_count": random.randint(25, 70),
        "event_type": "suspicious_login",
        "is_new_ip": 1,
        "is_new_device": 1,
    })
    return event


def generate_request_flood_event():
    event = _base_event()
    event.update({
        "username": random.choice(["guest", "bot_user", "unknown"]),
        "ip_address": random.choice(ATTACK_IPS),
        "location": "Unknown",
        "device_type": "Linux PC",
        "browser": "Chrome",
        "status": "FAILED",
        "failed_attempts": random.randint(2, 6),
        "request_count": random.randint(100, 300),
        "event_type": "request_flood",
        "is_new_ip": 1,
        "is_new_device": 1,
    })
    return event


def generate_event():
    choice = random.choices(
        population=["normal", "bruteforce", "suspicious", "flood"],
        weights=[60, 15, 15, 10],
        k=1
    )[0]

    if choice == "normal":
        return generate_normal_event()
    if choice == "bruteforce":
        return generate_bruteforce_event()
    if choice == "suspicious":
        return generate_suspicious_login_event()
    return generate_request_flood_event()