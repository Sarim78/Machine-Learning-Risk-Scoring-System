import pickle
import pandas as pd

# Load model
with open("models/risk_model.pkl", "rb") as f:
    model = pickle.load(f)

# Feature importance
importance = model.feature_importances_

features = ["income", "credit_utilization", "missed_payments", "account_age"]
explain_df = pd.DataFrame({
    "Feature": features,
    "Importance": importance
})

explain_df.to_csv("outputs/feature_importance.csv", index=False)

print("Explainable AI output generated.")
