from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Load trained machine learning model (if applicable)
try:
    model = pickle.load(open("model.pkl", "rb"))
except:
    model = None  # Model not available

@app.route('/predict', methods=['POST'])
def predict():
    """ Predicts electricity usage and suggests optimizations """
    data = request.json
    features = np.array(data['features']).reshape(1, -1)

    if model:
        prediction = model.predict(features)
        return jsonify({'prediction': prediction.tolist()})
    return jsonify({'error': 'Model not available'})

@app.route('/track_usage', methods=['POST'])
def track_usage():
    """ Tracks electricity usage and calculates remaining budget """
    data = request.json
    monthly_limit = data['monthly_limit']
    current_usage = data['current_usage']

    remaining = monthly_limit - current_usage
    return jsonify({'remaining_budget': remaining, 'status': 'OK'})

@app.route('/toggle_appliance', methods=['POST'])
def toggle_appliance():
    """ Simulates smart appliance control """
    data = request.json
    appliance = data['appliance']
    action = data['action']

    return jsonify({'message': f"{appliance} has been turned {action}."})

if __name__ == '__main__':
    app.run(debug=True)
