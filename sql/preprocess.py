import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load raw data
df = pd.read_csv("data/raw_data.csv")

# Separate features and target
X = df.drop("default", axis=1)
y = df["default"]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

processed_df = pd.DataFrame(X_scaled, columns=X.columns)
processed_df["default"] = y

# Save processed data
processed_df.to_csv("data/processed_data.csv", index=False)

print("Data preprocessing completed.")
