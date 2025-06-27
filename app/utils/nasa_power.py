# solar_api/utils/nasa_power.py

import requests

def fetch_nasa_power_data(lat: float, lon: float, start: str, end: str):
    url = "https://power.larc.nasa.gov/api/temporal/hourly/point"
    params = {
        "parameters": "GHI,DNI,DHI,T2M,WS2M",
        "community": "RE",
        "longitude": lon,
        "latitude": lat,
        "start": start,
        "end": end,
        "format": "JSON"
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data["properties"]["parameter"]
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
