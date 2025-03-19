import requests
import json
import random
import time

# Backend Flask server URL
backend_url = "http://127.0.0.1:5000/esp32_status"

def generate_sensor_data():
    """Simulates voltage, current, and power readings."""
    voltage = round(random.uniform(210, 230), 2)
    current = round(random.uniform(5, 15), 2)
    power = round(voltage * current, 2)

    return {"voltage": voltage, "current": current, "power": power}

def send_data():
    """Sends simulated sensor data to the backend server."""
    while True:
        sensor_data = generate_sensor_data()
        try:
            response = requests.post(backend_url, json=sensor_data)
            if response.status_code == 200:
                print(f"✅ Data sent successfully: {sensor_data}")
            else:
                print(f"❌ Failed to send data. Status code: {response.status_code}")
                print("Response:", response.text)  # Print server response for debugging
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Connection Error: {e}")

        time.sleep(5)

if __name__ == "__main__":
    print("📡 Starting ESP32 simulation...")
    send_data()
