import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

# Load cleaned training data
df = pd.read_csv("../data/train_cleaned.csv")

y = df["SalePrice"]
X = df.drop("SalePrice", axis=1)

# Train model
model = RandomForestRegressor(n_estimators=200, max_depth=20, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "house_price_model.pkl")

print("✅ Model saved as house_price_model.pkl")
