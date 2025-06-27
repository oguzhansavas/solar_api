# Solar Irradiance Historical API

This is a FastAPI-based microservice that provides access to historical solar irradiance data using NASA POWER.

## Features

- Fetch hourly GHI, DNI, DHI, temperature, and wind speed
- Input coordinates (latitude, longitude) and time range
- Simple RESTful endpoints for easy integration
- Returns data in JSON format
- Supports historical queries

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
   GET /v1/irradiance/historical?lat=40.0&lon=29.0&start=20240601&end=20240602
   ```

## Endpoints

- `/v1/irradiance/historical`: Get historical solar irradiance and weather data for a given location and time range.

## Input Parameters

- `lat` (float): Latitude
- `lon` (float): Longitude
- `start` (YYYYMMDD): Start date in YYYYMMDD format
- `end` (YYYYMMDD): End date in YYYYMMDD format
- `include_poa` (bool, optional): Include plane of array calculation (default: False)

## Output

Returns a JSON object with hourly values for:
- GHI (Global Horizontal Irradiance)
- DNI (Direct Normal Irradiance)
- DHI (Diffuse Horizontal Irradiance)
- Temperature
- Wind Speed