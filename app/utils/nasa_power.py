# solar_api/utils/nasa_power.py

import requests

USER_PARAM_MAP = {
    "total_irradiance": "ALLSKY_SFC_SW_DWN",
    "clear_sky_irradiance": "CLRSKY_SFC_SW_DWN",
    "temperature": "T2M",
    "wind_speed": "WS2M",
    "relative_humidity": "RH2M",
    "precipitation": "PRECTOTCORR",
    "surface_pressure": "PS",
    "cloud_cover": "CLOUD_AMT"
}

def fetch_nasa_power_data(
    lat: float,
    lon: float,
    start: str,
    end: str,
    user_param: str = "temperature",
    community: str = "RE"
):
    nasa_param = USER_PARAM_MAP.get(user_param)
    if not nasa_param:
        return {"error": f"Unknown parameter '{user_param}'. Valid options: {list(USER_PARAM_MAP.keys())}"}
    url = "https://power.larc.nasa.gov/api/temporal/hourly/point"
    params = {
        "parameters": nasa_param,
        "community": community,
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
        print("NASA API response:", data)  # For debugging
        if (
            "properties" in data and
            "parameter" in data["properties"] and
            nasa_param in data["properties"]["parameter"] and
            "parameters" in data and
            nasa_param in data["parameters"] and
            "units" in data["parameters"][nasa_param]
        ):
            parameter_data = data["properties"]["parameter"][nasa_param]
            unit = data["parameters"][nasa_param]["units"]
            return {"data": parameter_data, "unit": unit}
        if "errors" in data:
            return {"error": data["errors"]}
        return {"error": "Unexpected response format from NASA POWER API."}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
