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
import json

app = Flask(__name__)
CORS(app)

# Mock database file
DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "monthly_limit": 100,  # Default monthly limit in kWh
            "current_usage": 0,    # Current total usage in kWh
            "appliance_status": {},  # Tracks ON/OFF status
            "appliance_data": {  # Default appliances with power ratings in kW
                "Air Conditioner": {"power": 1.5, "usage": 0},
                "Refrigerator": {"power": 0.2, "usage": 0},
                "Washing Machine": {"power": 0.5, "usage": 0},
                "Television": {"power": 0.1, "usage": 0},
                "Fan": {"power": 0.075, "usage": 0}
            }
        }

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Route to update the monthly limit
@app.route('/set_limit', methods=['POST'])
def set_limit():
    request_data = request.get_json()
    data = load_data()
    
    if "monthly_limit" in request_data:
        data["monthly_limit"] = request_data["monthly_limit"]
        save_data(data)
        return jsonify({"message": "Monthly limit updated successfully"}), 200
    
    return jsonify({"error": "Invalid request"}), 400

# Route to get usage and remaining budget
@app.route('/get_usage', methods=['GET'])
def get_usage():
    data = load_data()
    remaining_budget = data["monthly_limit"] - data["current_usage"]
    return jsonify({
        "current_usage": data["current_usage"],
        "remaining_budget": remaining_budget,
        "monthly_limit": data["monthly_limit"],
        "appliance_data": data["appliance_data"]
    })

# Route to toggle appliance ON/OFF
@app.route('/toggle_appliance', methods=['POST'])
def toggle_appliance():
    data = load_data()
    request_data = request.get_json()

    appliance = request_data.get("appliance")
    action = request_data.get("action")

    if not appliance or not action:
        return jsonify({"error": "Invalid request"}), 400

    data["appliance_status"][appliance] = action

    # Simulate power consumption if appliance is ON
    if action == "ON":
        power = data["appliance_data"][appliance]["power"]
        data["appliance_data"][appliance]["usage"] += power  # Increment usage

    save_data(data)

    return jsonify({"message": f"{appliance} turned {action.upper()}"}), 200

if __name__ == '__main__':
    app.run(debug=True)


