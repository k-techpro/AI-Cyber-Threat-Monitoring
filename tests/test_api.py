import requests

def test_api():
    r = requests.get("http://127.0.0.1:8000/")
    print(r.json())

if __name__ == "__main__":
    test_api()