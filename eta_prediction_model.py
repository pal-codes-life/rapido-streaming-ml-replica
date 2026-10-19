import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Load telemetry dataset
data = pd.read_csv("rapido_telemetry.csv")

# 2. One-hot encode categorical zones (pickup and drop locations)
processed_data = pd.get_dummies(data, columns=["pickup_zone", "drop_zone"], drop_first=True)

# Select training features (exclude metadata and target variables)
feature_cols = [c for c in processed_data.columns if c not in [
    "ride_id", "timestamp", "actual_eta_mins", "surge_multiplier"
]]

X = processed_data[feature_cols]
y = processed_data["actual_eta_mins"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Fit Random Forest Regressor
eta_model = RandomForestRegressor(n_estimators=120, max_depth=6, random_state=42)
eta_model.fit(X_train, y_train)

# 4. Evaluate performance
preds = eta_model.predict(X_test)
mae = mean_absolute_error(y_test, preds)
r2 = r2_score(y_test, preds)

print("--- Trip ETA Prediction Model Evaluation ---")
print(f"Mean Absolute Error (MAE): {mae:.2f} minutes")
print(f"R-squared Score (R2): {r2:.4f}")