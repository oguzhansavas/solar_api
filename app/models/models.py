from pydantic import BaseModel
from typing import List, Dict, Any

class IrradianceData(BaseModel):
    GHI: float
    DNI: float
    DHI: float
    Temperature: float
    Wind_Speed: float

class IrradianceResponse(BaseModel):
    location: Dict[str, float]
    irradiance: List[IrradianceData]