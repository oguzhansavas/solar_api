# Solar Irradiance Forecast API

This is a FastAPI-based microservice that provides access to historical and forecasted solar irradiance data using NASA POWER.

## Features

- Fetch hourly GHI, DNI, DHI, temperature, and wind speed
- Input coordinates (latitude, longitude) and time range
- Simple RESTful endpoints for easy integration
- Returns data in JSON format
- Supports both historical and forecast queries

## Usage

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run the API:**
   ```
   uvicorn main:app --reload
   ```

3. **Example request:**
   ```
   GET /irradiance?lat=40.0&lon=29.0&start=2024-06-01T00:00:00Z&end=2024-06-02T00:00:00Z
   ```

## Endpoints

- `/irradiance`: Get solar irradiance and weather data for a given location and time range.

## Input Parameters

- `lat` (float): Latitude
- `lon` (float): Longitude
- `start` (ISO8601): Start datetime
- `end` (ISO8601): End datetime

## Output

Returns a JSON object with hourly values for:
- GHI (Global Horizontal Irradiance)
- DNI (Direct Normal Irradiance)
- DHI (Diffuse Horizontal Irradiance)
- Temperature
- Wind Speed