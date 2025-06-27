# solar_api/main.py

from fastapi import FastAPI, Query
from typing import Optional
import uvicorn
from utils.nasa_power import fetch_nasa_power_data
from models.models import IrradianceResponse

app = FastAPI(title="Solar Irradiance Forecast API")

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
    include_poa: Optional[bool] = False,
):
    data = fetch_nasa_power_data(lat, lon, start, end)
    return {"location": {"lat": lat, "lon": lon}, "irradiance": data}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
