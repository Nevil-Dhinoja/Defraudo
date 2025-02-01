from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from flask_cors import CORS
import numpy as np
from geopy.distance import geodesic

# Load the trained model and encoders
model = joblib.load('fraud_detection_model.pkl')
le_userID = joblib.load('user_encoder.pkl')
le_deviceID = joblib.load('device_encoder.pkl')

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Feature engineering functions
def calculate_location_change(row, prev_row):
    if prev_row is None:
        return 0
    return geodesic((row['latitude'], row['longitude']), (prev_row['latitude'], prev_row['longitude'])).meters

def apply_location_change(group):
    prev_row = None
    location_changes = []
    for _, row in group.iterrows():
        location_changes.append(calculate_location_change(row, prev_row))
        prev_row = row
    group['location_change'] = location_changes
    return group

@app.route('/predict', methods=['POST'])
def predict_fraud():
    data = request.get_json()

    userID = data.get('userID')
    amount = data.get('amount')
    location = data.get('location')
    deviceID = data.get('deviceID')
    time = data.get('time')  

    if not all([userID, amount, location, deviceID, time]):
        return jsonify({"success": False, "message": "Missing transaction data."}), 400

    # Encode categorical data using the label encoders
    if userID not in le_userID.classes_:
        le_userID.classes_ = np.append(le_userID.classes_, userID)
    userID_encoded = le_userID.transform([userID])[0]

    if deviceID not in le_deviceID.classes_:
        le_deviceID.classes_ = np.append(le_deviceID.classes_, deviceID)
    deviceID_encoded = le_deviceID.transform([deviceID])[0]

    # Location encoding (Optional: Using hash here or another method)
    location_encoded = hash(location) % 100000

    # Prepare transaction data for prediction (with necessary features)
    # Create a DataFrame to simulate feature engineering as done during training
    transaction = pd.DataFrame({
        'amount': [amount],
        'userID': [userID_encoded],
        'time': [time],
        'location': [location_encoded],
        'deviceID': [deviceID_encoded]
    })

    # Convert timestamp to milliseconds (similar to what was done during training)
    transaction['timestamp_ms'] = transaction['time'].astype(np.int64) // 10**6

    # Calculate transaction_gap (time difference between current and previous transaction for each user)
    transaction['transaction_gap'] = 0  # In the real case, you would calculate this from the history of the user
    # Calculate location_change (distance between current and previous transaction)
    transaction['location_change'] = 0  # This would also need to be calculated from historical data

    # Ensure all features match the training set
    features = ['transaction_gap', 'location_change', 'timestamp_ms', 'userID', 'deviceID']
    transaction = transaction[features]

    # Predict fraud
    prediction = model.predict(transaction)
    is_fraud = bool(prediction[0])

    # Return the result as JSON
    return jsonify({"isFraud": is_fraud})

if __name__ == '__main__':
    app.run(debug=True)