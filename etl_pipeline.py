import pandas as pd
from sqlalchemy import create_engine, text
import os

# ── 1. EXTRACT ──────────────────────────────────────────────
def extract_data():
    df = pd.read_csv("customer_data.csv")
    print(f"✅ Extracted {len(df)} records from CSV")
    return df

# ── 2. TRANSFORM ────────────────────────────────────────────
def transform_data(df):
    # Drop duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df["monthly_charges"] = df["monthly_charges"].fillna(df["monthly_charges"].mean())
    df["total_charges"] = df["total_charges"].fillna(df["total_charges"].mean())

    # Add churn label column
    df["churn_label"] = df["churned"].apply(lambda x: "Yes" if x == 1 else "No")

    # Add customer risk score
    df["risk_score"] = (
        (df["num_complaints"] * 10) +
        (df["monthly_charges"] * 0.5) -
        (df["tenure_months"] * 0.3)
    ).round(2)

    # Flag high risk customers
    df["high_risk"] = df["risk_score"].apply(lambda x: True if x > 50 else False)

    print(f"✅ Transformed data — {df['churned'].sum()} churned customers found")
    return df

# ── 3. LOAD ─────────────────────────────────────────────────
def load_data(df):
    # Save to CSV as output
    df.to_csv("transformed_customer_data.csv", index=False)
    print("✅ Loaded — saved to transformed_customer_data.csv")

# ── 4. RUN PIPELINE ─────────────────────────────────────────
if __name__ == "__main__":
    print("🚀 Starting ETL Pipeline...")
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)
    print("🎉 ETL Pipeline completed successfully!")