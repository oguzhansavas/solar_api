# Solar Irradiance Forecast API

A FastAPI microservice for retrieving **historical** solar irradiance and weather data from NASA POWER, and for **forecasting** solar irradiance using machine learning and Open-Meteo weather forecasts.

## Features

- Fetch hourly historical data for total/clear-sky irradiance, temperature, wind speed, humidity, precipitation, and cloud cover
- Forecast hourly total irradiance up to 7 days ahead using weather forecasts and solar geometry
- User-friendly parameter names (e.g., `total_irradiance`, `temperature`)
- Specify coordinates, time range, and NASA community (`RE` or `SB`)
- Returns data and units in JSON

---

## Example Requests

### Historical Data

```
GET /v1/irradiance/historical?lat=52.3676&lon=4.9041&start=20240101&end=20240102&parameters=total_irradiance&community=SB
```

### Forecast Data

```
GET /v1/irradiance/forecast?lat=52.3676&lon=4.9041&start=2025070800&end=2025071400
```

---

## Parameters

### Historical Endpoint

- `lat` (float): Latitude
- `lon` (float): Longitude
- `start` (YYYYMMDD): Start date
- `end` (YYYYMMDD): End date
- `parameters` (str): One of `total_irradiance`, `clear_sky_irradiance`, `temperature`, `wind_speed`, `relative_humidity`, `precipitation`, `cloud_cover`
- `community` (str, optional): `RE` or `SB`

### Forecast Endpoint

- `lat` (float): Latitude
- `lon` (float): Longitude
- `start` (YYYYMMDDHH): Forecast start datetime (UTC)
- `end` (YYYYMMDDHH): Forecast end datetime (UTC, max 7 days after start)
- **Note:** The forecast endpoint currently supports only locations within the Benelux region (Netherlands, Belgium, Luxembourg).

---

## Response

### Historical Example

```json
{
  "location": {"lat": 52.3676, "lon": 4.9041},
  "unit": "W/m²",
  "irradiance": {
    "2024010108": 19.42,
    "2024010109": 65.2,
    ...
  }
}
```

### Forecast Example

```json
{
  "location": {"lat": 52.3676, "lon": 4.9041},
  "unit": "W/m²",
  "forecast": {
    "2025-07-08 00:00": 0.0,
    "2025-07-08 01:00": 0.0,
    "2025-07-08 02:00": 0.0,
    "2025-07-08 03:00": 0.0,
    "2025-07-08 04:00": 12.3,
    "2025-07-08 05:00": 120.7,
    ...
  }
}
```

---

## Notes

- Forecasts are set to zero at night (when the sun is below the horizon).
- **Forecasting is currently limited to the Benelux region.**