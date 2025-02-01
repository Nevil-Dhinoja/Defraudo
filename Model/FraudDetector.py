import pandas as pd
import random
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

csv_file_path = r'D:\project\Model\fraud_detection_dataset_large.csv'
df = pd.read_csv(csv_file_path)

df = df.dropna()  # You can also fill missing values using df.fillna()

label_encoder_userID = LabelEncoder()
label_encoder_location = LabelEncoder()
label_encoder_deviceID = LabelEncoder()

df['userID'] = label_encoder_userID.fit_transform(df['userID'])
df['location'] = label_encoder_location.fit_transform(df['location'])
df['deviceID'] = label_encoder_deviceID.fit_transform(df['deviceID'])
df['time'] = pd.to_datetime(df['time']).astype(int)  # Convert time to integer for modeling

X = df.drop('isFraud', axis=1)  # Features
y = df['isFraud']  # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test, y_pred))

random_userID = [f"user_{random.randint(1, 50)}" for _ in range(5)]
random_location = [f"location_{random.randint(1, 10)}" for _ in range(5)]
random_deviceID = [f"device_{random.randint(1, 20)}" for _ in range(5)]

random_userID_encoded = label_encoder_userID.transform(random_userID)
random_location_encoded = label_encoder_location.transform(random_location)
random_deviceID_encoded = label_encoder_deviceID.transform(random_deviceID)

random_transactions = pd.DataFrame({
    'amount': [random.randint(5, 1000) for _ in range(5)],  # 5 random transactions
    'userID': random_userID_encoded,
    'time': [int((datetime.now() - timedelta(minutes=random.randint(0, 1440))).timestamp() * 1000) for _ in range(5)],  # Convert to milliseconds since epoch
    'location': random_location_encoded,
    'deviceID': random_deviceID_encoded
})


random_predictions = model.predict(random_transactions)

print("\nRandom Transactions Predictions:")
for i, transaction in random_transactions.iterrows():
    print(f"Transaction {i+1}:")
    print(f"Amount: {transaction['amount']}, UserID: {random_userID[i]}, "
          f"Location: {random_location[i]}, DeviceID: {random_deviceID[i]}, "
          f"Predicted Fraud: {'Fraud' if random_predictions[i] == 1 else 'Not Fraud'}\n")

import joblib
joblib.dump(model, 'fraud_detection_model.pkl')
