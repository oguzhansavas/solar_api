---
layout: default
title: Getting Started
nav_order: 2
permalink: /getting-started/
description: Quick start guide for the Solar Irradiance Forecast API with examples and basic usage patterns.
---

## 🚀 Quick Start

The Solar Irradiance Forecast API provides two main endpoints for accessing solar irradiance data:

1. **Historical Data** - Get past solar irradiance and weather data (global coverage)
2. **Forecast Data** - Get 7-day solar irradiance predictions (Benelux region)

### Base URL
```
{{ site.api_base_url }}
```

## 📊 Your First API Call

Let's start with a simple example to get historical solar irradiance data for Amsterdam:

```bash
curl "{{ site.api_base_url }}/v1/irradiance/historical?lat={{ site.example_lat }}&lon={{ site.example_lon }}&start=20240101&end=20240102&parameters=total_irradiance"
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

This will return:

```json
{
  "location": {"lat": 52.3676, "lon": 4.9041},
  "unit": "W/m²",
  "irradiance": {
    "2024010100": 0.0,
    "2024010101": 0.0,
    "2024010108": 19.42,
    "2024010109": 65.2,
    "2024010110": 128.6,
    "2024010111": 201.5,
    "2024010112": 245.8,
    "2024010113": 267.3,
    "2024010114": 251.9,
    "2024010115": 198.1,
    "2024010116": 112.4,
    "2024010117": 34.7,
    "2024010118": 0.0
  }
}
```

## 🔮 Forecast Example

Get a 24-hour solar irradiance forecast for Amsterdam:

```bash
curl "{{ site.api_base_url }}/v1/irradiance/forecast?lat={{ site.example_lat }}&lon={{ site.example_lon }}&start=2025070800&end=2025070900"
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

## 🛠️ API Integration Examples

### Python Example

```python
import requests
import json

# Historical data example
def get_historical_irradiance(lat, lon, start_date, end_date):
    url = "{{ site.api_base_url }}/v1/irradiance/historical"
    params = {
        "lat": lat,
        "lon": lon,
        "start": start_date,
        "end": end_date,
        "parameters": "total_irradiance",
        "community": "SB"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Usage
data = get_historical_irradiance({{ site.example_lat }}, {{ site.example_lon }}, "20240101", "20240102")
if data:
    print(f"Location: {data['location']}")
    print(f"Unit: {data['unit']}")
    print(f"Data points: {len(data['irradiance'])}")
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

## 📋 Parameter Reference

### Required Parameters

All endpoints require these basic parameters:

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `lat` | float | Latitude coordinate | `{{ site.example_lat }}` |
| `lon` | float | Longitude coordinate | `{{ site.example_lon }}` |

### Historical Endpoint Parameters

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `start` | string | Yes | Start date (YYYYMMDD) | `20240101` |
| `end` | string | Yes | End date (YYYYMMDD) | `20240102` |
| `parameters` | string | Yes | Data parameter to retrieve | `total_irradiance` |
| `community` | string | No | NASA POWER community (`RE` or `SB`) | `SB` |

#### Available Parameters

- `total_irradiance` - Total solar irradiance (W/m²)
- `clear_sky_irradiance` - Clear-sky solar irradiance (W/m²)
- `temperature` - Air temperature (°C)
- `wind_speed` - Wind speed (m/s)
- `relative_humidity` - Relative humidity (%)
- `precipitation` - Precipitation (mm/hour)
- `cloud_cover` - Cloud cover (%)

### Forecast Endpoint Parameters

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `start` | string | Yes | Start datetime (YYYYMMDDHH) | `2025070800` |
| `end` | string | Yes | End datetime (YYYYMMDDHH) | `2025071400` |

**Note:** Forecast endpoint currently supports only locations within the Benelux region.

## 🌍 Coverage Areas

### Historical Data
- **Coverage**: Worldwide
- **Source**: NASA POWER database
- **Resolution**: Hourly data
- **Available from**: 1981 to near real-time

### Forecast Data  
- **Coverage**: Benelux region (Netherlands, Belgium, Luxembourg)
- **Forecast horizon**: Up to 7 days
- **Resolution**: Hourly forecasts
- **Model**: Machine learning based on weather forecasts

## ⚡ Rate Limits & Best Practices

### Rate Limits
- No strict rate limits for reasonable usage
- Bulk requests should be spaced appropriately
- Consider caching responses when possible

### Best Practices

> 1. **Use appropriate date ranges**: Don't request more data than needed
> 2. **Cache responses**: Store frequently accessed data locally
> 3. **Handle errors gracefully**: Always check response status codes
> 4. **Respect the service**: Avoid excessive concurrent requests

### Error Handling

```python
import requests

def safe_api_call(url, params):
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return None
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

## 🚀 Next Steps

Now that you're familiar with the basics:

1. [**📚 Explore API Reference**]({{ '/api-reference/' | relative_url }}) - Detailed endpoint documentation
2. [**💻 View Examples**]({{ '/examples/' | relative_url }}) - Real-world use cases and code samples  
3. [**🌍 Check Coverage**]({{ '/coverage/' | relative_url }}) - Understand regional limitations
4. [**🆘 Get Support**]({{ '/support/' | relative_url }}) - Community and technical support

## 💡 Tips for Success

> - Start with historical data to understand the API structure
> - Use the health endpoint (`/health`) to verify API availability
> - Test your coordinates with small date ranges first
> - Consider time zones: all data is in UTC
> - For production use, implement proper error handling and retries

<script>
function copyToClipboard(text) {
  navigator.clipboard.writeText(text.trim()).then(function() {
    // Show a temporary success message
    console.log('Copied to clipboard');
  });
}
</script>
