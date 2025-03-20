# import requests
# import json
# import random
# import time

# # Backend Flask server URL
# backend_url = "http://127.0.0.1:5000/esp32_status"

# def generate_sensor_data():
#     """Simulates voltage, current, and power readings."""
#     voltage = round(random.uniform(210, 230), 2)
#     current = round(random.uniform(5, 15), 2)
#     power = round(voltage * current, 2)

#     return {"voltage": voltage, "current": current, "power": power}

# def send_data():
#     """Sends simulated sensor data to the backend server."""
#     while True:
#         sensor_data = generate_sensor_data()
#         try:
#             response = requests.post(backend_url, json=sensor_data)
#             if response.status_code == 200:
#                 print(f"✅ Data sent successfully: {sensor_data}")
#             else:
#                 print(f"❌ Failed to send data. Status code: {response.status_code}")
#                 print("Response:", response.text)  # Print server response for debugging
#         except requests.exceptions.RequestException as e:
#             print(f"⚠️ Connection Error: {e}")

#         time.sleep(5)

# if __name__ == "__main__":
#     print("📡 Starting ESP32 simulation...")
#     send_data()

# END OF FIRST CODE

#include <WiFi.h>
#include <HTTPClient.h>

import requests
import time

SERVER_URL = "http://127.0.0.1:5000"  # Flask server URL

def send_energy_data(energy_used):
    """Simulates ESP32 sending energy consumption data."""
    payload = {"energy_consumed": energy_used}
    try:
        response = requests.post(f"{SERVER_URL}/esp32_status", json=payload)
        print(f"Sent: {payload}, Response: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print("Error sending data:", e)

def check_appliance_control():
    """Simulates ESP32 checking if an appliance should be turned ON/OFF."""
    try:
        response = requests.get(f"{SERVER_URL}/get_usage")
        data = response.json()
        
        # Simulate turning appliances on/off based on remaining budget
        remaining_budget = data.get("remaining_budget", 0)
        if remaining_budget < 5:  # If energy is low, turn off appliances
            print("Energy low! Turning off all appliances.")
        else:
            print("Sufficient energy. Appliances can run normally.")

    except requests.exceptions.RequestException as e:
        print("Error checking appliance control:", e)

if __name__ == "__main__":
    while True:
        send_energy_data(2.5)  # Simulate sending 2.5 kWh usage
        check_appliance_control()  # Check appliance status
        time.sleep(5)  # Run every 5 seconds



