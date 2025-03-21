import requests
import random
import time

# Flask server endpoint (Ensure app.py is running)
SERVER_URL = "http://127.0.0.1:5000/pi_status"

def generate_sensor_data():
    """Simulates Raspberry Pi reading voltage, current, and power."""
    voltage = round(random.uniform(210, 230), 2)  # Simulated voltage (V)
    current = round(random.uniform(5, 15), 2)    # Simulated current (A)
    power = round((voltage * current) / 1000, 2)  # Convert to kWh

    return {
        "voltage": voltage,
        "current": current,
        "power": power,
        "energy_consumed": power
    }

def send_energy_data():
    """Sends simulated sensor data to Flask backend every 5 seconds."""
    while True:
        sensor_data = generate_sensor_data()
        try:
            response = requests.post(SERVER_URL, json=sensor_data)
            if response.status_code == 200:
                print(f"📡 Sent: {sensor_data}")
            else:
                print(f"⚠️ Failed to send data. Server responded with {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Error sending data: {e}")

        time.sleep(5)  # Wait 5 seconds before sending new data

if __name__ == "__main__":
    print("🚀 Raspberry Pi Simulator Running...")
    send_energy_data()
