# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import json

# app = Flask(__name__)
# CORS(app)

# # Mock database file
# DATA_FILE = "data.json"

# def load_data():
#     try:
#         with open(DATA_FILE, "r") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {"monthly_limit": 1000, "current_usage": 0, "appliance_status": {}}

# def save_data(data):
#     with open(DATA_FILE, "w") as file:
#         json.dump(data, file, indent=4)

# # Route to receive ESP32 data and update usage
# @app.route('/esp32_status', methods=['POST'])
# def esp32_status():
#     request_data = request.get_json()
#     data = load_data()
    
#     # Ensure "current_usage" is updated
#     if "energy_consumed" in request_data:
#         data["current_usage"] = request_data["energy_consumed"]

#     save_data(data)
#     print("✅ Received ESP32 Data:", request_data)  # Debugging log
#     return jsonify({"message": "ESP32 data received successfully"}), 200

# # Route to get usage and remaining budget
# @app.route('/get_usage', methods=['GET'])
# def get_usage():
#     data = load_data()
#     remaining_budget = data["monthly_limit"] - data["current_usage"]
#     return jsonify({"current_usage": data["current_usage"], "remaining_budget": remaining_budget})

# # Route to toggle appliance ON/OFF
# @app.route('/toggle_appliance', methods=['POST'])
# def toggle_appliance():
#     data = load_data()
#     request_data = request.get_json()

#     appliance = request_data.get("appliance")
#     action = request_data.get("action")

#     if not appliance or not action:
#         return jsonify({"error": "Invalid request"}), 400

#     data["appliance_status"][appliance] = action
#     save_data(data)

#     return jsonify({"message": f"{appliance} turned {action.upper()}"}), 200

# if __name__ == '__main__':
#     app.run(debug=True)

#End of FIRST code

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import json

# app = Flask(__name__)
# CORS(app)

# # Mock database file
# DATA_FILE = "data.json"

# def load_data():
#     try:
#         with open(DATA_FILE, "r") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {"monthly_limit": 1000, "current_usage": 0, "appliance_status": {}}

# def save_data(data):
#     with open(DATA_FILE, "w") as file:
#         json.dump(data, file, indent=4)

# # Route to receive ESP32 data and update usage
# @app.route('/esp32_status', methods=['POST'])
# def esp32_status():
#     request_data = request.get_json()
#     data = load_data()
    
#     # Increment usage instead of resetting
#     if "energy_consumed" in request_data:
#         data["current_usage"] += request_data["energy_consumed"]

#     save_data(data)
#     print("✅ Updated ESP32 Data:", request_data)  # Debugging log
#     return jsonify({"message": "ESP32 data received successfully"}), 200

# # Route to get usage and remaining budget
# @app.route('/get_usage', methods=['GET'])
# def get_usage():
#     data = load_data()
#     remaining_budget = data["monthly_limit"] - data["current_usage"]
#     return jsonify({"current_usage": data["current_usage"], "remaining_budget": remaining_budget})

# # Route to toggle appliance ON/OFF
# @app.route('/toggle_appliance', methods=['POST'])
# def toggle_appliance():
#     data = load_data()
#     request_data = request.get_json()

#     appliance = request_data.get("appliance")
#     action = request_data.get("action")

#     if not appliance or not action:
#         return jsonify({"error": "Invalid request"}), 400

#     data["appliance_status"][appliance] = action
#     save_data(data)

#     return jsonify({"message": f"{appliance} turned {action.upper()}"}), 200

# if __name__ == '__main__':
#     app.run(debug=True)

# END of SECOND  code

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import json

# app = Flask(__name__)
# CORS(app)

# # Mock database file
# DATA_FILE = "data.json"

# def load_data():
#     try:
#         with open(DATA_FILE, "r") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {"monthly_limit": 100, "current_usage": 0, "appliance_status": {}}

# def save_data(data):
#     with open(DATA_FILE, "w") as file:
#         json.dump(data, file, indent=4)

# # Route to update the monthly limit
# @app.route('/set_limit', methods=['POST'])
# def set_limit():
#     request_data = request.get_json()
#     data = load_data()
    
#     if "monthly_limit" in request_data:
#         data["monthly_limit"] = request_data["monthly_limit"]
#         save_data(data)
#         return jsonify({"message": "Monthly limit updated successfully"}), 200
    
#     return jsonify({"error": "Invalid request"}), 400

# # Route to get usage and remaining budget
# @app.route('/get_usage', methods=['GET'])
# def get_usage():
#     data = load_data()
#     remaining_budget = data["monthly_limit"] - data["current_usage"]
#     return jsonify({"current_usage": data["current_usage"], "remaining_budget": remaining_budget, "monthly_limit": data["monthly_limit"]})

# # Route to receive ESP32 data and update usage
# @app.route('/esp32_status', methods=['POST'])
# def esp32_status():
#     request_data = request.get_json()
#     data = load_data()
    
#     # Ensure "current_usage" is updated
#     if "energy_consumed" in request_data:
#         data["current_usage"] = request_data["energy_consumed"]

#     save_data(data)
#     print("✅ Received ESP32 Data:", request_data)  # Debugging log
#     return jsonify({"message": "ESP32 data received successfully"}), 200

# # Route to toggle appliance ON/OFF
# @app.route('/toggle_appliance', methods=['POST'])
# def toggle_appliance():
#     data = load_data()
#     request_data = request.get_json()

#     appliance = request_data.get("appliance")
#     action = request_data.get("action")

#     if not appliance or not action:
#         return jsonify({"error": "Invalid request"}), 400

#     data["appliance_status"][appliance] = action
#     save_data(data)

#     return jsonify({"message": f"{appliance} turned {action.upper()}"}), 200

# if __name__ == '__main__':
#     app.run(debug=True)

# end of THIRD code

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simulated database
energy_data = {
    "monthly_limit": 100,  # Default limit in kWh
    "current_usage": 0,    # Energy used so far
    "remaining_budget": 100,
    "appliances": [
        {"name": "Air Conditioner", "usage": 2},
        {"name": "Refrigerator", "usage": 0.8},
        {"name": "Washing Machine", "usage": 1.5},
        {"name": "Television", "usage": 0.2},
        {"name": "Fan", "usage": 0.1}
    ]
}

@app.route("/get_usage", methods=["GET"])
def get_usage():
    """Returns current electricity usage data."""
    energy_data["remaining_budget"] = max(0, energy_data["monthly_limit"] - energy_data["current_usage"])
    return jsonify(energy_data)

@app.route("/set_limit", methods=["POST"])
def set_limit():
    """Updates the monthly electricity limit."""
    data = request.json
    energy_data["monthly_limit"] = data.get("monthly_limit", energy_data["monthly_limit"])
    return jsonify({"message": "Monthly limit updated successfully!"})

@app.route("/toggle_appliance", methods=["POST"])
def toggle_appliance():
    """Toggles an appliance ON/OFF."""
    data = request.json
    appliance_name = data.get("appliance")
    status = data.get("status")

    if status == "ON":
        energy_data["current_usage"] += next((a["usage"] for a in energy_data["appliances"] if a["name"] == appliance_name), 0)
    
    return jsonify({"message": f"{appliance_name} turned {status}"})

@app.route("/esp32_status", methods=["POST"])
def esp32_status():
    """Receives data from ESP32."""
    data = request.json
    energy_consumed = data.get("energy_consumed", 0)
    energy_data["current_usage"] += energy_consumed
    return jsonify({"message": "ESP32 data received"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)




