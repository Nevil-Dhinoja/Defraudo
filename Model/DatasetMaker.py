import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import string

def generate_user_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=24))  

def generate_fraud_detection_dataset(num_users, num_transactions, fraud_ratio, location_type, device_switching, fraud_pattern, country=None):
    user_ids = [generate_user_id() for _ in range(num_users)]  
    device_ids = [f"device_{i}" for i in range(1, num_users + 1)]

    transactions = []
    start_time = datetime(2023, 1, 1)

    for _ in range(num_transactions):
        user_id = random.choice(user_ids)
        device_id = random.choice(device_ids) if device_switching == "Occasional" or random.random() > 0.1 else random.choice(device_ids)  # Device switching based on behavior
        amount = round(random.uniform(5, 5000), 2)  # Random transaction amount

        # Random timestamp within a year
        timestamp = start_time + timedelta(seconds=random.randint(0, 60 * 60 * 24 * 365))  
        
        # Random location (Worldwide or a Single Country)
        if location_type == "Worldwide":
            latitude = round(random.uniform(-90, 90), 6)
            longitude = round(random.uniform(-180, 180), 6)
        elif location_type == "Single Country" and country:
            latitude, longitude = get_location_from_country(country)  

        is_fraud = random.random() < fraud_ratio  

        if fraud_pattern == "Bursts":
            if is_fraud and random.random() < 0.8:  
                is_fraud = True
            else:
                is_fraud = False

        transactions.append({
            "userID": user_id,
            "amount": amount,
            "timestamp": timestamp.isoformat(),
            "latitude": latitude,
            "longitude": longitude,
            "deviceID": device_id,
            "isFraud": is_fraud
        })

    df = pd.DataFrame(transactions)
    return df

def get_location_from_country(country):
    if country == "USA":
        return round(random.uniform(24.396308, 49.384358), 6), round(random.uniform(-125.0, -66.93457), 6)
    elif country == "India":
        return round(random.uniform(6.746, 35.513), 6), round(random.uniform(68.1766, 97.4025), 6)
    # Add other countries as needed
    return round(random.uniform(-90, 90), 6), round(random.uniform(-180, 180), 6)

# Example Usage:
num_users = 100
num_transactions = 200000
fraud_ratio = 0.1  # 10% fraud transactions
location_type = "Worldwide"  # Or "Single Country" with a country name
device_switching = "Occasional"  # Or "Frequent"
fraud_pattern = "Randomly Distributed"  # Or "Bursts"
country = "USA"  # Used only if location_type is "Single Country"

df = generate_fraud_detection_dataset(num_users, num_transactions, fraud_ratio, location_type, device_switching, fraud_pattern, country)

df.to_csv("fraud_detection_dataset.csv", index=False)

print(df.head())
