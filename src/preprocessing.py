import os 
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Path to the dataset
RAW_PATH = os.path.join("data", "raw", "credit.csv")
PROCESSED_PATH = os.path.join("data", "processed", "cleaned_data.csv")

# Define the required columns for the dataset
REQUIRED_COLUMNS = [
    "checking_balance",       
    "months_loan_duration",
    "credit_history",
    "purpose",
    "amount",
    "savings_balance",
    "employment_duration",
    "years_at_residence",
    "age",
    "other_credit",
    "housing",
    "existing_loans_count",   
    "job", 
    "dependents",
    "phone",
    "default",
]

NUMERIC_COLUMNS = [
    "months_loan_duration",
    "amount",
    "percent_of_income",
    "years_at_residence",
    "age",
    "existing_loans_count",
    "dependents",
]
 
CATEGORICAL_COLUMNS = [
    "checking_balance",
    "credit_history",
    "purpose",
    "savings_balance",
    "employment_duration",
    "other_credit",
    "housing",
    "job",
    "phone",
]

def preprocess_data(raw_path=RAW_PATH, processed_path=PROCESSED_PATH):
    pass 

def load_data(path):
    pass

def validate_schema(df):
    pass

def encode_target(df):
    pass

def handle_missing_values(df):
    pass

def remove_outliers(df, z_thresh = 3.5):
    pass

def encode_categoricals(df):
    pass

def engineer_features(df):
    pass

def scale_numerics(df):
    pass

def save_data(df, path):
    pass

if __name__ == "__main__":
    preprocess_data()