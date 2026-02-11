import pandas as pd
import pickle

# Load model
with open("models/risk_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load data
df = pd.read_csv("data/processed_data.csv")
X = df.drop("default", axis=1)

# Predict risk probabilities
df["risk_score"] = model.predict_proba(X)[:, 1]

# Save predictions for Power BI
df.to_csv("outputs/predictions.csv", index=False)

print("Risk scores generated.")
