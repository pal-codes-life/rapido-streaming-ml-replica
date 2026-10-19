import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor

# 1. Load telemetry dataset
data = pd.read_csv("rapido_telemetry.csv")

# 2. Select predictive features
features = ["hour_of_day", "is_peak_hour", "demand_requests", "available_drivers", "supply_demand_ratio"]
target = "surge_multiplier"

X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train XGBoost Regressor
surge_model = XGBRegressor(n_estimators=100, max_depth=4, learning_rate=0.08, random_state=42)
surge_model.fit(X_train, y_train)

# 4. Evaluate Model Performance
predictions = surge_model.predict(X_test)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print("--- Dynamic Surge Pricing Model Evaluation ---")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R-squared Score (R2): {r2:.4f}")

# Test with a high-demand scenario
sample_event = pd.DataFrame([{
    "hour_of_day": 18,
    "is_peak_hour": 1,
    "demand_requests": 220,
    "available_drivers": 45,
    "supply_demand_ratio": 4.88
}])
predicted_surge = surge_model.predict(sample_event)[0]
print(f"\nSimulated High Congestion Surge Multiplier: {predicted_surge:.2f}x")