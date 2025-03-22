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
        {"name": "Air Conditioner", "usage": 2.0, "voltage": 220, "status": "OFF"},
        {"name": "Refrigerator", "usage": 0.8, "voltage": 230, "status": "OFF"},
        {"name": "Washing Machine", "usage": 1.5, "voltage": 220, "status": "OFF"},
        {"name": "Television", "usage": 0.2, "voltage": 110, "status": "OFF"},
        {"name": "Fan", "usage": 0.1, "voltage": 120, "status": "OFF"}
    ]
}

def update_remaining_budget():
    """Updates remaining budget dynamically based on current usage."""
    energy_data["remaining_budget"] = max(0, energy_data["monthly_limit"] - energy_data["current_usage"])

    # Calculate how long each appliance can run within the budget
    for appliance in energy_data["appliances"]:
        if appliance["usage"] > 0:
            appliance["remaining_hours"] = round(energy_data["remaining_budget"] / appliance["usage"], 2)
        else:
            appliance["remaining_hours"] = 0

def ai_recommendation():
    """AI recommends turning off appliances when usage is high."""
    update_remaining_budget()
    
    if energy_data["current_usage"] > energy_data["monthly_limit"] * 0.9:
        sorted_appliances = sorted(energy_data["appliances"], key=lambda x: -x["usage"])
        for appliance in sorted_appliances:
            if appliance["status"] == "ON":
                appliance["status"] = "OFF"
                energy_data["current_usage"] -= appliance["usage"]
                update_remaining_budget()
                return f"⚠️ High usage detected! {appliance['name']} was turned OFF to save power."
        return "⚠️ Energy usage is too high! All the appliances are turned off."
    elif energy_data["current_usage"] > energy_data["monthly_limit"] * 0.7:
        return "⚠️ Energy usage is approaching the limit. Appliances are going to be turned off soon.."
    
    return "✅ Energy usage is optimal."

@app.route("/get_usage", methods=["GET"])
def get_usage():
    """Returns current electricity usage data."""
    update_remaining_budget()
    recommendation = ai_recommendation()
    return jsonify({**energy_data, "recommendation": recommendation})

@app.route("/set_limit", methods=["POST"])
def set_limit():
    """Updates the monthly electricity limit."""
    data = request.json
    new_limit = data.get("monthly_limit")

    if new_limit and new_limit > 0:
        energy_data["monthly_limit"] = new_limit
        update_remaining_budget()
        return jsonify({"message": "Monthly limit updated successfully!"}), 200
    return jsonify({"error": "Invalid limit"}), 400

@app.route("/toggle_appliance", methods=["POST"])
def toggle_appliance():
    """Turns an appliance ON/OFF and updates usage correctly."""
    data = request.json
    appliance_name = data.get("appliance")
    status = data.get("status")

    for appliance in energy_data["appliances"]:
        if appliance["name"] == appliance_name:
            appliance["status"] = status  # Update status

    # Update current usage based on ON appliances
    energy_data["current_usage"] = sum(a["usage"] for a in energy_data["appliances"] if a["status"] == "ON")
    update_remaining_budget()

    return jsonify({"message": f"{appliance_name} turned {status}", "current_usage": energy_data["current_usage"]})

@app.route("/pi_status", methods=["POST"])
def pi_status():
    """Receives data from Raspberry Pi and updates usage dynamically."""
    data = request.json
    if not data or "energy_consumed" not in data:
        return jsonify({"error": "Invalid data"}), 400

    energy_consumed = data["energy_consumed"]
    energy_data["current_usage"] += energy_consumed
    update_remaining_budget()

    return jsonify({"message": "Raspberry Pi data received successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
