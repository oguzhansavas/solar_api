import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pvlib.solarposition import get_solarposition
from sklearn.metrics import mean_squared_error
import lightgbm as lgb
import joblib
from sklearn.model_selection import GridSearchCV
import xgboost as xgb

from app.utils.nasa_power import fetch_nasa_power_data

# --- Config ---
LOCATIONS = [
    {"city": "Amsterdam", "lat": 52.3676, "lon": 4.9041}
]

START_DATE = "2022-01-01"
END_DATE = "2025-03-30"
OUTPUT_MODEL_PATH = "app/models/irradiance_forecast_model.pkl"

# --- Functions ---
def fetch_data(lat, lon, start_date, end_date, community="SB"):
    # Fetch all crucial parameters using user-friendly names
    params = [
        "total_irradiance",
        "clear_sky_irradiance",
        "temperature",
        "relative_humidity",
        "precipitation",
        "cloud_cover"
    ]
    data_dict = {}
    for param in params:
        result = fetch_nasa_power_data(
            lat, lon,
            start_date.replace("-", ""),
            end_date.replace("-", ""),
            user_param=param,
            community=community
        )
        if "error" in result:
            raise ValueError(f"Error fetching {param}: {result['error']}")
        data_dict[param] = result["data"]
    # Convert to DataFrame
    df = pd.DataFrame(data_dict)
    df.index = pd.to_datetime(df.index, format="%Y%m%d%H")
    return df

def add_features(df, lat, lon):
    df = df.copy()
    df["hour"] = df.index.hour
    df["dayofyear"] = df.index.dayofyear
    df["month"] = df.index.month
    df["sin_doy"] = np.sin(2 * np.pi * df["dayofyear"] / 365)
    df["cos_doy"] = np.cos(2 * np.pi * df["dayofyear"] / 365)
    solpos = get_solarposition(df.index, lat, lon)
    df["solar_zenith"] = solpos["zenith"].values
    df["lat"] = lat
    df["lon"] = lon
    # Only lag features for cloud cover (since you can forecast it)
    for lag in [1, 2, 3, 24, 48, 72]:
        df[f"cloud_cover_lag{lag}"] = df["cloud_cover"].shift(lag)
    return df

# --- Aggregate training data ---
all_data = []
for loc in LOCATIONS:
    print(f"Fetching data for {loc['city']}...")
    raw = fetch_data(loc["lat"], loc["lon"], START_DATE, END_DATE)
    enriched = add_features(raw, loc["lat"], loc["lon"])
    # Predict total irradiance directly (target is total_irradiance shifted -24h for day-ahead)
    enriched["irradiance_target"] = enriched["total_irradiance"].shift(-24)
    all_data.append(enriched)

# --- Combine and clean ---
df_all = pd.concat(all_data)
df_all = df_all.dropna(subset=["irradiance_target"])

# --- Train model ---
features = [
    "temperature", "relative_humidity", "precipitation", "cloud_cover",
    "solar_zenith", "sin_doy", "cos_doy", "lat", "lon",
    "cloud_cover_lag1", "cloud_cover_lag2", "cloud_cover_lag3",
    "cloud_cover_lag24", "cloud_cover_lag48", "cloud_cover_lag72"
]
df_all = df_all.sort_index()
df_all = df_all.dropna(subset=features + ["irradiance_target"])
split_point = int(len(df_all) * 0.95)
X_train = df_all.iloc[:split_point][features]
y_train = df_all.iloc[:split_point]["irradiance_target"]
X_val = df_all.iloc[split_point:][features]
y_val = df_all.iloc[split_point:]["irradiance_target"]

# --- Hyperparameter tuning ---
param_grid = {
    "n_estimators": np.arange(50, 301, 50).tolist(),
    "max_depth": np.arange(3, 11).tolist(),
    "learning_rate": [0.01, 0.05, 0.1]
}
base_model = xgb.XGBRegressor(tree_method="hist", random_state=42)
grid_search = GridSearchCV(base_model, param_grid, cv=3, scoring="neg_mean_squared_error", n_jobs=-1)
grid_search.fit(X_train, y_train)
print(f"Best params: {grid_search.best_params_}")

# Use the best estimator for predictions
model = grid_search.best_estimator_

# --- Evaluation ---
y_pred_irradiance = model.predict(X_val)
rmse_irradiance = np.sqrt(mean_squared_error(y_val, y_pred_irradiance))
print(f"Validation RMSE (Total Irradiance): {rmse_irradiance:.4f}")

# Visualize predictions: Total Irradiance
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.plot(y_val.index, y_val, label='Actual Irradiance', color='blue')
plt.plot(y_val.index, y_pred_irradiance, label='Predicted Irradiance', color='orange')
plt.title('Total Irradiance Prediction vs Actual')
plt.xlabel('Date')
plt.ylabel('Total Irradiance (W/m²)')
plt.legend()
plt.show()

# --- Save model ---
os.makedirs(os.path.dirname(OUTPUT_MODEL_PATH), exist_ok=True)
joblib.dump(model, OUTPUT_MODEL_PATH)
print(f"Model saved to {OUTPUT_MODEL_PATH}")
