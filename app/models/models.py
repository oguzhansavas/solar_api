from pydantic import BaseModel
from typing import Dict, Any

class IrradianceResponse(BaseModel):
    location: Dict[str, float]
    irradiance: Dict[str, Any]
    unit: str