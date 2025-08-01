---
layout: page
title: API Reference
permalink: /api-reference/
description: Complete API reference documentation for the Solar Irradiance Forecast API endpoints, parameters, and responses.
---

## API Overview

The Solar Irradiance Forecast API provides RESTful endpoints for accessing solar irradiance data. All endpoints return JSON responses and use HTTP GET requests.

**Base URL:** `{{ site.api_base_url }}`  
**API Version:** `{{ site.api_version }}`

---

## 📊 Historical Data Endpoint {#historical}

Retrieve historical solar irradiance and weather data from NASA POWER database.

### Endpoint
```
GET /v1/irradiance/historical
```

### Parameters

<div class="param-card">
  <h4>lat <span class="param-type">float</span> <span class="param-required">required</span></h4>
  <p>Latitude coordinate in decimal degrees (-90 to 90)</p>
  <p><strong>Example:</strong> <code>{{ site.example_lat }}</code></p>
</div>

<div class="param-card">
  <h4>lon <span class="param-type">float</span> <span class="param-required">required</span></h4>
  <p>Longitude coordinate in decimal degrees (-180 to 180)</p>
  <p><strong>Example:</strong> <code>{{ site.example_lon }}</code></p>
</div>

<div class="param-card">
  <h4>start <span class="param-type">string</span> <span class="param-required">required</span></h4>
  <p>Start date in YYYYMMDD format</p>
  <p><strong>Example:</strong> <code>20240101</code></p>
</div>

<div class="param-card">
  <h4>end <span class="param-type">string</span> <span class="param-required">required</span></h4>
  <p>End date in YYYYMMDD format</p>
  <p><strong>Example:</strong> <code>20240102</code></p>
</div>

<div class="param-card">
  <h4>parameters <span class="param-type">string</span> <span class="param-required">required</span></h4>
  <p>Parameter to retrieve. Available options:</p>
  <ul>
    <li><code>total_irradiance</code> - Total solar irradiance (W/m²)</li>
    <li><code>clear_sky_irradiance</code> - Clear-sky solar irradiance (W/m²)</li>
    <li><code>temperature</code> - Air temperature (°C)</li>
    <li><code>wind_speed</code> - Wind speed (m/s)</li>
    <li><code>relative_humidity</code> - Relative humidity (%)</li>
    <li><code>precipitation</code> - Precipitation (mm/hour)</li>
    <li><code>cloud_cover</code> - Cloud cover (%)</li>
  </ul>
  <p><strong>Example:</strong> <code>total_irradiance</code></p>
</div>

<div class="param-card">
  <h4>community <span class="param-type">string</span> <span style="background: #6c757d; color: white; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.8rem; font-weight: 600; margin-left: 0.5rem;">optional</span></h4>
  <p>NASA POWER community. Options:</p>
  <ul>
    <li><code>RE</code> - Renewable Energy (default)</li>
    <li><code>SB</code> - Sustainable Buildings</li>
  </ul>
  <p><strong>Default:</strong> <code>RE</code></p>
</div>

### Example Request

```bash
curl "{{ site.api_base_url }}/v1/irradiance/historical?lat={{ site.example_lat }}&lon={{ site.example_lon }}&start=20240101&end=20240102&parameters=total_irradiance&community=SB"
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

### Response Format

```json
{
  "location": {
    "lat": 52.3676,
    "lon": 4.9041
  },
  "unit": "W/m²",
  "irradiance": {
    "2024010100": 0.0,
    "2024010101": 0.0,
    "2024010102": 0.0,
    "2024010103": 0.0,
    "2024010104": 0.0,
    "2024010105": 0.0,
    "2024010106": 0.0,
    "2024010107": 0.0,
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
    "2024010118": 0.0,
    "2024010119": 0.0,
    "2024010120": 0.0,
    "2024010121": 0.0,
    "2024010122": 0.0,
    "2024010123": 0.0
  }
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `location.lat` | float | Requested latitude |
| `location.lon` | float | Requested longitude |
| `unit` | string | Unit of measurement |
| `irradiance` | object | Hourly data with timestamp keys (YYYYMMDDHH) |

---

## 🔮 Forecast Data Endpoint {#forecast}

Get solar irradiance forecasts for up to 7 days ahead using machine learning models.

### Endpoint
```
GET /v1/irradiance/forecast
```

### Parameters

<div class="param-card">
  <h4>lat <span class="param-type">float</span> <span class="param-required">required</span></h4>
  <p>Latitude coordinate in decimal degrees (Benelux region only)</p>
  <p><strong>Example:</strong> <code>{{ site.example_lat }}</code></p>
</div>

<div class="param-card">
  <h4>lon <span class="param-type">float</span> <span class="param-required">required</span></h4>
  <p>Longitude coordinate in decimal degrees (Benelux region only)</p>
  <p><strong>Example:</strong> <code>{{ site.example_lon }}</code></p>
</div>

<div class="param-card">
  <h4>start <span class="param-type">string</span> <span class="param-required">required</span></h4>
  <p>Forecast start datetime in YYYYMMDDHH format (UTC)</p>
  <p><strong>Example:</strong> <code>2025070800</code> (July 8, 2025 at 08:00 UTC)</p>
</div>

<div class="param-card">
  <h4>end <span class="param-type">string</span> <span class="param-required">required</span></h4>
  <p>Forecast end datetime in YYYYMMDDHH format (UTC). Maximum 7 days after start.</p>
  <p><strong>Example:</strong> <code>2025071400</code> (July 14, 2025 at 00:00 UTC)</p>
</div>

### Coverage Limitations

⚠️ **Important:** The forecast endpoint currently supports only locations within the Benelux region:
- **Netherlands** (latitude: 50.7 to 53.6, longitude: 3.2 to 7.2)
- **Belgium** (latitude: 49.5 to 51.5, longitude: 2.5 to 6.4)
- **Luxembourg** (latitude: 49.4 to 50.2, longitude: 5.7 to 6.5)

### Example Request

```bash
curl "{{ site.api_base_url }}/v1/irradiance/forecast?lat={{ site.example_lat }}&lon={{ site.example_lon }}&start=2025070800&end=2025070900"
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

### Response Format

```json
{
  "location": {
    "lat": 52.3676,
    "lon": 4.9041
  },
  "unit": "W/m²",
  "forecast": {
    "2025-07-08 08:00": 120.45,
    "2025-07-08 09:00": 245.78,
    "2025-07-08 10:00": 387.23,
    "2025-07-08 11:00": 512.89,
    "2025-07-08 12:00": 634.12,
    "2025-07-08 13:00": 598.34,
    "2025-07-08 14:00": 467.56,
    "2025-07-08 15:00": 312.78,
    "2025-07-08 16:00": 189.45,
    "2025-07-08 17:00": 87.23,
    "2025-07-08 18:00": 23.45,
    "2025-07-08 19:00": 0.0,
    "2025-07-08 20:00": 0.0,
    "2025-07-08 21:00": 0.0,
    "2025-07-08 22:00": 0.0,
    "2025-07-08 23:00": 0.0,
    "2025-07-09 00:00": 0.0
  }
}
```

### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `location.lat` | float | Requested latitude |
| `location.lon` | float | Requested longitude |
| `unit` | string | Unit of measurement (W/m²) |
| `forecast` | object | Hourly forecast data with ISO datetime keys |

---

## 🏥 Health Check Endpoint

Check API service availability.

### Endpoint
```
GET /health
```

### Example Request

```bash
curl "{{ site.api_base_url }}/health"
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

### Response

```json
{
  "status": "ok"
}
```

---

## 🚨 Error Responses

All endpoints may return the following error responses:

### HTTP Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | OK | Request successful |
| 400 | Bad Request | Invalid parameters or request format |
| 422 | Unprocessable Entity | Valid request format but invalid data |
| 500 | Internal Server Error | Server-side error |
| 502 | Bad Gateway | External service unavailable |

### Error Response Format

```json
{
  "detail": "Error description"
}
```

### Common Errors

#### Invalid Coordinates
```json
{
  "detail": "Invalid latitude or longitude values"
}
```

#### Date Format Error
```json
{
  "detail": "Invalid date format. Use YYYYMMDD for historical or YYYYMMDDHH for forecast"
}
```

#### Forecast Region Error
```json
{
  "detail": "Forecast service is currently limited to Benelux region"
}
```

#### Forecast Horizon Error
```json
{
  "detail": "Forecast horizon cannot exceed 7 days."
}
```

---

## 📝 OpenAPI Specification

For programmatic access to the API specification, you can access the automatically generated OpenAPI/Swagger documentation:

- **Swagger UI:** `{{ site.api_base_url }}/docs`
- **OpenAPI JSON:** `{{ site.api_base_url }}/openapi.json`

---

## 💡 Implementation Notes

### Time Zones
- All timestamps are in **UTC**
- Historical data timestamps format: `YYYYMMDDHH`
- Forecast data timestamps format: `YYYY-MM-DD HH:MM`

### Data Sources
- **Historical Data:** NASA POWER database
- **Forecast Data:** Open-Meteo weather forecasts + ML models
- **Update Frequency:** Historical data updated daily, forecasts updated every 6 hours

### Precision
- Coordinates precision: up to 6 decimal places
- Irradiance values precision: 2 decimal places
- Forecast values are automatically set to 0 when sun is below horizon

### Performance
- Typical response time: 100-500ms for historical data
- Typical response time: 200-800ms for forecast data
- Rate limiting: No strict limits for reasonable usage

<script>
function copyToClipboard(text) {
  navigator.clipboard.writeText(text.trim()).then(function() {
    console.log('Copied to clipboard');
  });
}
</script>