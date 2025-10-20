import requests

def test_predict_endpoint(ip_address, port=8080):
    payload = {
        "data": [
            [5.1, 3.5, 1.4, 0.2],
            [6.7, 3.0, 5.2, 2.3]
        ]
    }

    print("Sending request to /predict endpoint...")

    try:
        response = requests.post(f"http://{ip_address}:{port}/predict", json=payload)
        response.raise_for_status()
        predictions = response.json()
        print("Predictions:", predictions)
        return True
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return False


IP = "127.0.0.1"
PORT = 8000

test_predict_endpoint(IP, PORT)
