# solar_api/main.py

from fastapi import FastAPI, Query, HTTPException
from typing import Optional
import uvicorn
from app.utils.nasa_power import fetch_nasa_power_data
from app.models.models import IrradianceResponse
import joblib
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pvlib.solarposition import get_solarposition
from pvlib.location import Location
import requests

app = FastAPI(title="Solar Irradiance Forecast API")

MODEL_PATH = "app/models/irradiance_forecast_model.pkl"
model = joblib.load(MODEL_PATH)

def fetch_open_meteo_forecast(lat, lon, start, end):
    start_dt = datetime.strptime(start, "%Y%m%d%H")
    end_dt = datetime.strptime(end, "%Y%m%d%H")
    if (end_dt - start_dt).days > 7:
        raise HTTPException(status_code=400, detail="Forecast horizon cannot exceed 7 days.")
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&hourly=temperature_2m,relative_humidity_2m,cloud_cover,precipitation"
        f"&start_date={start_dt.strftime('%Y-%m-%d')}"
        f"&end_date={end_dt.strftime('%Y-%m-%d')}"
        f"&timezone=UTC"
    )
    resp = requests.get(url)
    if not resp.ok:
        raise HTTPException(status_code=502, detail="Failed to fetch weather forecast from Open-Meteo.")
    data = resp.json()
    df = pd.DataFrame({
        "time": data["hourly"]["time"],
        "temperature": data["hourly"]["temperature_2m"],
        "relative_humidity": data["hourly"]["relative_humidity_2m"],
        "cloud_cover": data["hourly"]["cloud_cover"],
        "precipitation": data["hourly"]["precipitation"],
    })
    df["time"] = pd.to_datetime(df["time"])
    df = df.set_index("time")
    return df

def fetch_clear_sky_irradiance(index, lat, lon):
    location = Location(lat, lon)
    clearsky = location.get_clearsky(index, model='ineichen')
    return clearsky["ghi"]

def add_forecast_features(df, lat, lon):
    df = df.copy()
    df["hour"] = df.index.hour
    df["dayofyear"] = df.index.dayofyear
    df["sin_doy"] = np.sin(2 * np.pi * df["dayofyear"] / 365)
    df["cos_doy"] = np.cos(2 * np.pi * df["dayofyear"] / 365)
    solpos = get_solarposition(df.index, lat, lon)
    df["solar_zenith"] = solpos["zenith"].values
    df["lat"] = lat
    df["lon"] = lon
    # Lag features for cloud cover (pad with NaN for forecast)
    for lag in [1, 2, 3, 24, 48, 72]:
        df[f"cloud_cover_lag{lag}"] = df["cloud_cover"].shift(lag)
    return df

@app.get(
    "/v1/irradiance/historical",
    summary="Get historical solar irradiance data",
    response_model=IrradianceResponse
)
def get_irradiance(
    lat: float = Query(...),
    lon: float = Query(...),
    start: str = Query(..., description="Start date in YYYYMMDD format"),
    end: str = Query(..., description="End date in YYYYMMDD format"),
    parameters: str = Query("T2M", description="Comma-separated list of parameters"),
    community: str = Query("RE", description="Community (RE or SB)"),
):
    result = fetch_nasa_power_data(lat, lon, start, end, parameters, community)
    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=422, detail=result["error"])
    return {
        "location": {"lat": lat, "lon": lon},
        "unit": result["unit"],
        "irradiance": result["data"]
    }

@app.get("/v1/irradiance/forecast")
def forecast_irradiance(
    lat: float = Query(...),
    lon: float = Query(...),
    start: str = Query(..., description="Forecast start in YYYYMMDDHH"),
    end: str = Query(..., description="Forecast end in YYYYMMDDHH (max 7 days after start)"),
):
    df_weather = fetch_open_meteo_forecast(lat, lon, start, end)
    df_feat = add_forecast_features(df_weather, lat, lon)
    features = [
        "temperature", "relative_humidity", "precipitation", "cloud_cover",
        "solar_zenith", "sin_doy", "cos_doy", "lat", "lon",
        "cloud_cover_lag1", "cloud_cover_lag2", "cloud_cover_lag3",
        "cloud_cover_lag24", "cloud_cover_lag48", "cloud_cover_lag72"
    ]
    X = df_feat[features].dropna()
    y_pred_irradiance = model.predict(X)
    return {
        "location": {"lat": lat, "lon": lon},
        "unit": "W/m²",
        "forecast": {
            k: float(v) for k, v in zip(X.index.strftime("%Y-%m-%d %H:%M"), y_pred_irradiance.round(2))
        }
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
