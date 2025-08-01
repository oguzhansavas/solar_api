---
layout: page
title: Coverage & Availability
permalink: /coverage/
description: Understand the geographical coverage, regional limitations, and data availability for historical and forecast endpoints.
---

## 🌍 Coverage Overview

The Solar Irradiance Forecast API provides different coverage areas for historical and forecast data, each optimized for specific data sources and model capabilities.

---

## 📊 Historical Data Coverage

### Global Availability
Historical solar irradiance and weather data is available **worldwide** through NASA POWER database integration.

<div class="feature-card">
  <h3>🌐 Worldwide Coverage</h3>
  <ul>
    <li><strong>Latitude Range:</strong> -90° to +90° (South Pole to North Pole)</li>
    <li><strong>Longitude Range:</strong> -180° to +180° (Complete global coverage)</li>
    <li><strong>Resolution:</strong> 0.5° x 0.625° (approximately 50km x 50km grid)</li>
    <li><strong>Data Source:</strong> NASA POWER (Prediction of Worldwide Energy Resources)</li>
  </ul>
</div>

### Available Parameters
All locations worldwide support the following parameters:

| Parameter | Description | Unit | Global Coverage |
|-----------|-------------|------|-----------------|
| `total_irradiance` | Total solar irradiance | W/m² | ✅ Yes |
| `clear_sky_irradiance` | Clear-sky solar irradiance | W/m² | ✅ Yes |
| `temperature` | Air temperature at 2m | °C | ✅ Yes |
| `wind_speed` | Wind speed at 10m | m/s | ✅ Yes |
| `relative_humidity` | Relative humidity | % | ✅ Yes |
| `precipitation` | Precipitation | mm/hour | ✅ Yes |
| `cloud_cover` | Cloud cover | % | ✅ Yes |

### Temporal Coverage
- **Start Date:** January 1, 1981
- **End Date:** Near real-time (typically 1-3 days behind current date)
- **Resolution:** Hourly data
- **Update Frequency:** Daily updates

### Example Locations
Test the historical endpoint with these example coordinates:

```bash
# Europe - Amsterdam, Netherlands
curl "{{ site.api_base_url }}/v1/irradiance/historical?lat=52.3676&lon=4.9041&start=20240101&end=20240102&parameters=total_irradiance"

# North America - New York, USA
curl "{{ site.api_base_url }}/v1/irradiance/historical?lat=40.7128&lon=-74.0060&start=20240101&end=20240102&parameters=total_irradiance"

# Asia - Tokyo, Japan
curl "{{ site.api_base_url }}/v1/irradiance/historical?lat=35.6762&lon=139.6503&start=20240101&end=20240102&parameters=total_irradiance"

# Africa - Cairo, Egypt
curl "{{ site.api_base_url }}/v1/irradiance/historical?lat=30.0444&lon=31.2357&start=20240101&end=20240102&parameters=total_irradiance"

# Australia - Sydney
curl "{{ site.api_base_url }}/v1/irradiance/historical?lat=-33.8688&lon=151.2093&start=20240101&end=20240102&parameters=total_irradiance"
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

---

## 🔮 Forecast Data Coverage

### Benelux Region Only
Solar irradiance forecasting is currently **limited to the Benelux region** due to model training and validation constraints.

<div class="feature-card" style="border-left-color: #FF8C00;">
  <h3>🇳🇱🇧🇪🇱🇺 Benelux Coverage Area</h3>
  <p><strong>Supported Countries:</strong></p>
  <ul>
    <li><strong>Netherlands:</strong> Latitude 50.7° to 53.6°, Longitude 3.2° to 7.2°</li>
    <li><strong>Belgium:</strong> Latitude 49.5° to 51.5°, Longitude 2.5° to 6.4°</li>
    <li><strong>Luxembourg:</strong> Latitude 49.4° to 50.2°, Longitude 5.7° to 6.5°</li>
  </ul>
  <p><strong>Model Optimization:</strong> Machine learning models trained specifically on Benelux weather patterns and solar geometry.</p>
</div>

### Why Benelux Only?

1. **Model Training**: ML models require regional weather pattern training
2. **Data Quality**: High-quality weather forecast data availability
3. **Validation**: Extensive validation against actual solar installations
4. **Climate Specificity**: Solar irradiance patterns vary significantly by climate zone

### Forecast Specifications

| Specification | Details |
|---------------|---------|
| **Forecast Horizon** | Up to 7 days ahead |
| **Resolution** | Hourly forecasts |
| **Update Frequency** | Every 6 hours |
| **Model Type** | XGBoost regression with weather features |
| **Input Features** | Temperature, humidity, cloud cover, precipitation, solar geometry |

### Example Benelux Locations

```bash
# Netherlands - Amsterdam
curl "{{ site.api_base_url }}/v1/irradiance/forecast?lat=52.3676&lon=4.9041&start=2025070800&end=2025070900"

# Netherlands - The Hague
curl "{{ site.api_base_url }}/v1/irradiance/forecast?lat=52.0705&lon=4.3007&start=2025070800&end=2025070900"

# Belgium - Brussels
curl "{{ site.api_base_url }}/v1/irradiance/forecast?lat=50.8503&lon=4.3517&start=2025070800&end=2025070900"

# Belgium - Antwerp
curl "{{ site.api_base_url }}/v1/irradiance/forecast?lat=51.2194&lon=4.4025&start=2025070800&end=2025070900"

# Luxembourg - Luxembourg City
curl "{{ site.api_base_url }}/v1/irradiance/forecast?lat=49.6117&lon=6.1319&start=2025070800&end=2025070900"
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

---

## 🗺️ Coverage Validation

### Check Location Support

Use this JavaScript function to validate if a location supports forecasting:

```javascript
function validateLocation(lat, lon) {
    const beneluxBounds = {
        netherlands: {
            latMin: 50.7, latMax: 53.6,
            lonMin: 3.2, lonMax: 7.2
        },
        belgium: {
            latMin: 49.5, latMax: 51.5,
            lonMin: 2.5, lonMax: 6.4
        },
        luxembourg: {
            latMin: 49.4, latMax: 50.2,
            lonMin: 5.7, lonMax: 6.5
        }
    };
    
    for (const [country, bounds] of Object.entries(beneluxBounds)) {
        if (lat >= bounds.latMin && lat <= bounds.latMax &&
            lon >= bounds.lonMin && lon <= bounds.lonMax) {
            return {
                supported: true,
                country: country,
                services: ['historical', 'forecast']
            };
        }
    }
    
    return {
        supported: false,
        services: ['historical'], // Historical always available
        reason: 'Forecast service limited to Benelux region'
    };
}

// Examples
console.log(validateLocation({{ site.example_lat }}, {{ site.example_lon }})); // Amsterdam
console.log(validateLocation(40.7128, -74.0060)); // New York (forecast not supported)
console.log(validateLocation(50.8503, 4.3517)); // Brussels (both supported)
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

### Python Location Validator

```python
def check_forecast_coverage(lat, lon):
    """Check if coordinates are within Benelux forecast coverage"""
    
    # Define Benelux boundaries
    regions = {
        'Netherlands': {
            'lat_range': (50.7, 53.6),
            'lon_range': (3.2, 7.2)
        },
        'Belgium': {
            'lat_range': (49.5, 51.5),
            'lon_range': (2.5, 6.4)
        },
        'Luxembourg': {
            'lat_range': (49.4, 50.2),
            'lon_range': (5.7, 6.5)
        }
    }
    
    for region, bounds in regions.items():
        lat_min, lat_max = bounds['lat_range']
        lon_min, lon_max = bounds['lon_range']
        
        if lat_min <= lat <= lat_max and lon_min <= lon <= lon_max:
            return {
                'forecast_available': True,
                'region': region,
                'message': f'Location within {region} - forecast available'
            }
    
    return {
        'forecast_available': False,
        'region': 'Outside Benelux',
        'message': 'Forecast not available - location outside Benelux region'
    }

# Test examples
locations = [
    ({{ site.example_lat }}, {{ site.example_lon }}, "Amsterdam"),
    (40.7128, -74.0060, "New York"), 
    (50.8503, 4.3517, "Brussels"),
    (51.2194, 4.4025, "Antwerp"),
    (49.6117, 6.1319, "Luxembourg City")
]

for lat, lon, name in locations:
    result = check_forecast_coverage(lat, lon)
    print(f"{name}: {result['message']}")
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

---

## 🛣️ Future Expansion Plans

### Upcoming Regions

- We're actively working to expand forecast coverage to additional regions in Europe.

### Model Improvements

- **Extended Horizon**: Expand from 7-day to 14-day forecasts  
- **Ensemble Models**: Multi-model forecasting for improved accuracy
- **Real-time Calibration**: Dynamic model adjustment based on recent performance

---

## 📈 Data Quality & Accuracy

### Historical Data Quality
- **Source Reliability**: NASA POWER database with extensive validation
- **Accuracy**: ±5-10% for solar irradiance in most regions
- **Completeness**: >99% data availability for most locations
- **Temporal Consistency**: Consistent methodology since 1981

### Forecast Accuracy (Benelux) (NEEDS TO BE UPDATED!!!)
Based on validation against actual solar installations:

| Forecast Period | MAE (W/m²) | RMSE (W/m²) | R² |
|-----------------|------------|-------------|-----|
| Day 1 | 45.2 | 78.5 | 0.89 |
| Day 2 | 62.8 | 95.3 | 0.84 |
| Day 3 | 78.4 | 112.7 | 0.78 |
| Day 4-7 | 95.1 | 135.9 | 0.71 |

### Accuracy Factors (NEEDS TO BE UPDATED!!!)
- **Clear Days**: Highest accuracy (>90% correlation)
- **Cloudy Days**: Moderate accuracy (~75% correlation)  
- **Transition Periods**: Lower accuracy during weather fronts
- **Seasonal Variation**: Better accuracy in summer months

---

## 🔧 Implementation Considerations

### Handling Coverage Limitations

```python
def smart_api_call(lat, lon, start_date, end_date=None):
    """Intelligently choose endpoint based on location and date range"""
    
    # Check if forecast is available for this location
    coverage = check_forecast_coverage(lat, lon)
    
    # Determine if this is a forecast request (future dates)
    from datetime import datetime
    start_dt = datetime.strptime(start_date, '%Y%m%d')
    is_future = start_dt.date() > datetime.now().date()
    
    if is_future and coverage['forecast_available']:
        # Use forecast endpoint
        start_str = start_date + "00"  # Add hour
        end_str = (end_date or start_date) + "23"
        return call_forecast_endpoint(lat, lon, start_str, end_str)
    elif not is_future:
        # Use historical endpoint
        return call_historical_endpoint(lat, lon, start_date, end_date)
    else:
        # Future date but no forecast coverage
        raise ValueError(f"Forecast not available for location ({lat}, {lon}). "
                        f"Forecast currently limited to Benelux region.")

def call_with_fallback(lat, lon, date_range):
    """Try forecast first, fallback to historical if needed"""
    try:
        return smart_api_call(lat, lon, *date_range)
    except ValueError as e:
        if "Forecast not available" in str(e):
            print(f"Falling back to historical data: {e}")
            # Use most recent historical data as proxy
            return call_historical_endpoint(lat, lon, date_range[0], date_range[1])
        raise
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

### Error Messages by Region

Common error responses when requesting forecast data outside Benelux:

```json
{
  "detail": "Forecast service is currently limited to Benelux region. Your coordinates (40.7128, -74.0060) are outside the supported area. Please use the historical endpoint for this location."
}
```

<script>
function copyToClipboard(text) {
  navigator.clipboard.writeText(text.trim()).then(function() {
    console.log('Copied to clipboard');
  });
}
</script>
