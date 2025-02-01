
# Fraud Detection System - Documentation

This document provides an overview of the patterns that define fraudulent and non-fraudulent transactions, as well as detailed test cases to validate the behavior of the fraud detection system. The test cases include both fraudulent and non-fraudulent transaction scenarios and are designed for use with Postman or any HTTP client tool.

---

## Patterns for Fraudulent Transactions
Fraudulent transactions are identified based on the following patterns:

1. **Unusual Transaction Amounts**:
   - Transactions significantly higher or lower than the user's typical amounts.

2. **New or Unfamiliar Device ID**:
   - Transactions initiated from a device not previously used by the user.

3. **Unfamiliar or Suspicious Location**:
   - Transactions originating from a location the user has not transacted in before.

4. **Odd Transaction Timing**:
   - Transactions at unusual hours (e.g., late at night or very early morning).

5. **Rapid Consecutive Transactions**:
   - Multiple transactions occurring in a short time frame with unusual patterns.

6. **Mismatch of Features**:
   - A combination of new device, location, and odd timing that deviates from the user's usual behavior.

---

## Patterns for Non-Fraudulent Transactions
Non-fraudulent transactions align with the following patterns:

1. **Consistent Transaction Amounts**:
   - Transactions within the user's typical range.

2. **Known Device ID**:
   - Transactions from devices frequently used by the user.

3. **Familiar Location**:
   - Transactions originating from the user's regular transaction locations.

4. **Normal Timing**:
   - Transactions made during the user's usual active hours.

5. **Expected Behavior**:
   - Transactions that match the user's historical patterns across all features.

---

## Test Cases
The following test cases can be used to validate the fraud detection system. Each test case includes a JSON payload to be sent to the `/predict` endpoint of the Flask API.

### Fraudulent Transactions

#### Test Case 1: High Amount, Unknown Location & Device
**Request Body**:
```json
{
    "userID": "user_1",
    "amount": 10000,
    "location": "unknown_loc",
    "deviceID": "new_device",
    "time": 1675032000
}
```
**Expected Response**:
```json
{
    "prediction": "Fraud",
    "message": "Transaction is blocked due to fraud suspicion."
}
```

#### Test Case 2: Odd Time & New Device
**Request Body**:
```json
{
    "userID": "user_2",
    "amount": 100,
    "location": "location_2",
    "deviceID": "new_device",
    "time": 1675035600
}
```
**Expected Response**:
```json
{
    "prediction": "Fraud",
    "message": "Transaction is blocked due to fraud suspicion."
}
```

#### Test Case 3: New Location at Unusual Time
**Request Body**:
```json
{
    "userID": "user_3",
    "amount": 500,
    "location": "new_location",
    "deviceID": "device_1",
    "time": 1675046400
}
```
**Expected Response**:
```json
{
    "prediction": "Fraud",
    "message": "Transaction is blocked due to fraud suspicion."
}
```

#### Test Case 4: Rapid Consecutive Transactions
**Request Body**:
```json
{
    "userID": "user_4",
    "amount": 2000,
    "location": "location_5",
    "deviceID": "device_4",
    "time": 1675040000
}
```
**Expected Response**:
```json
{
    "prediction": "Fraud",
    "message": "Transaction is blocked due to fraud suspicion."
}
```

---

### Non-Fraudulent Transactions

#### Test Case 1: Typical User Behavior
**Request Body**:
```json
{
    "userID": "user_1",
    "amount": 50,
    "location": "location_1",
    "deviceID": "device_1",
    "time": 1675038000
}
```
**Expected Response**:
```json
{
    "prediction": "Not Fraud",
    "message": "Transaction approved successfully."
}
```

#### Test Case 2: Normal Time and Location
**Request Body**:
```json
{
    "userID": "user_2",
    "amount": 30,
    "location": "location_2",
    "deviceID": "device_2",
    "time": 1675032000
}
```
**Expected Response**:
```json
{
    "prediction": "Not Fraud",
    "message": "Transaction approved successfully."
}
```

#### Test Case 3: Known Device and Time
**Request Body**:
```json
{
    "userID": "user_3",
    "amount": 100,
    "location": "location_3",
    "deviceID": "device_3",
    "time": 1675035000
}
```
**Expected Response**:
```json
{
    "prediction": "Not Fraud",
    "message": "Transaction approved successfully."
}
```

---

## How to Use in Postman
1. **Open Postman**.
2. Select the **POST** method.
3. Set the URL to `http://127.0.0.1:5000/predict`.
4. Go to the **Body** tab and select `raw` with `JSON` format.
5. Copy and paste one of the request bodies above into the text area.
6. Click **Send** to submit the request.
7. Verify the response matches the expected outcome.

---

## Notes
- Ensure the Flask app is running before testing.
- Monitor the logs for any errors or inconsistencies.
- Modify the test cases as needed to include additional scenarios or features.
