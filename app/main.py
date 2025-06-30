# solar_api/main.py

from fastapi import FastAPI, Query, HTTPException
from typing import Optional
import uvicorn
from app.utils.nasa_power import fetch_nasa_power_data
from app.models.models import IrradianceResponse

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
