# Solar Irradiance Historical API

A FastAPI microservice for retrieving historical solar irradiance and weather data from NASA POWER.

## Features

- Fetch hourly data for total/clear-sky irradiance, temperature, wind speed, humidity, precipitation, and pressure
- User-friendly parameter names (e.g., `total_irradiance`, `temperature`)
- Specify coordinates, time range, and NASA community (`RE` or `SB`)
- Returns data and units in JSON

**Example request:**
```
GET /v1/irradiance/historical?lat=52.3676&lon=4.9041&start=20240101&end=20240102&parameters=total_irradiance&community=SB
```

## Parameters

- `lat` (float): Latitude
- `lon` (float): Longitude
- `start` (YYYYMMDD): Start date
- `end` (YYYYMMDD): End date
- `parameters` (str): One of `total_irradiance`, `clear_sky_irradiance`, `temperature`, `wind_speed`, `relative_humidity`, `precipitation`, `surface_pressure`
- `community` (str): `RE` or `SB`

## Response

```json
{
  "location": {"lat": 52.3676, "lon": 4.9041},
  "unit": "W m-2",
  "irradiance": {
    "2024010108": 19.42,
    "2024010109": 65.2,
    ...
  }
```