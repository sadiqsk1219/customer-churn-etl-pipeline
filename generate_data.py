import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_customer_data(num_records=500):
    customers = []
    for i in range(num_records):
        customer = {
            "customer_id": i + 1,
            "name": fake.name(),
            "email": fake.email(),
            "age": random.randint(18, 70),
            "gender": random.choice(["Male", "Female"]),
            "tenure_months": random.randint(1, 60),
            "monthly_charges": round(random.uniform(20, 150), 2),
            "total_charges": round(random.uniform(100, 5000), 2),
            "num_complaints": random.randint(0, 10),
            "churned": random.choice([0, 1])
        }
        customers.append(customer)
    
    df = pd.DataFrame(customers)
    df.to_csv("customer_data.csv", index=False)
    print("✅ Data generated successfully! 500 customer records created.")
    return df

if __name__ == "__main__":
    generate_customer_data()