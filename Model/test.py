import pandas as pd  
import random
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.ensemble import RandomForestClassifier  # type: ignore
from sklearn.metrics import classification_report, accuracy_score  # type: ignore
from sklearn.preprocessing import LabelEncoder  # type: ignore
import joblib  

csv_file_path = r'D:\project\Model\fraud_detection_dataset_large.csv'
df = pd.read_csv(csv_file_path)

print("Columns in dataset:", df.columns)

required_columns = {'userID', 'deviceLocation', 'deviceID', 'time', 'isFraud'}
missing_columns = required_columns - set(df.columns)
if missing_columns:
    raise ValueError(f"Missing columns in dataset: {missing_columns}")

df = df.dropna()

label_encoders = {}
for col in ['userID', 'deviceLocation', 'deviceID']:
    label_encoders[col] = LabelEncoder()
    df[col] = label_encoders[col].fit_transform(df[col])

df['time'] = pd.to_datetime(df['time']).astype(int) // 10**9  # Convert to seconds since epoch

X = df.drop('isFraud', axis=1)
y = df['isFraud']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test, y_pred))

random_data = {
    'userID': label_encoders['userID'].transform([f"user_{random.randint(1, 50)}" for _ in range(5)]),
    'deviceLocation': label_encoders['deviceLocation'].transform([f"location_{random.randint(1, 10)}" for _ in range(5)]),
    'deviceID': label_encoders['deviceID'].transform([f"device_{random.randint(1, 20)}" for _ in range(5)]),
    'amount': [random.randint(5, 1000) for _ in range(5)],
    'time': [int((datetime.now() - timedelta(minutes=random.randint(0, 1440))).timestamp()) for _ in range(5)]
}
random_transactions = pd.DataFrame(random_data)

# Predict fraud
random_predictions = model.predict(random_transactions)

# Display results
print("\nRandom Transactions Predictions:")
for i, transaction in random_transactions.iterrows():
    print(f"Transaction {i+1}: Amount: {transaction['amount']}, UserID: {transaction['userID']}, "
          f"DeviceLocation: {transaction['deviceLocation']}, DeviceID: {transaction['deviceID']}, "
          f"Predicted Fraud: {'Fraud' if random_predictions[i] == 1 else 'Not Fraud'}")

# Save model
joblib.dump(model, 'fraud_detection_model.pkl')
