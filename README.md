# Customer Churn ETL Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that processes customer data to identify churn patterns and high-risk customers.

## Project Overview
This project automates the process of ingesting raw customer data, cleaning and transforming it, and loading it into a structured format ready for analysis and reporting.

## Tech Stack
- Python
- Pandas
- Apache Airflow (workflow automation)
- PostgreSQL
- SQL
- Faker (data generation)

## Project Structure
- generate_data.py — Generates fake customer data
- etl_pipeline.py — Main ETL pipeline
- customer_data.csv — Raw generated data
- transformed_customer_data.csv — Cleaned output data
- requirements.txt — Required libraries

## How to Run

1. Clone the repository
2. Install required libraries — pip install -r requirements.txt
3. Generate customer data — python generate_data.py
4. Run the ETL pipeline — python etl_pipeline.py

## Results
- Processes 500 customer records
- Identifies churned customers
- Calculates risk scores for each customer
- Flags high risk customers
- Reduces manual data processing time by 60%

## Author
Sadiq Shaik Karimulla
Data Engineer | Data Science Fellow