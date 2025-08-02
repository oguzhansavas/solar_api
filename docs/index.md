---
layout: default
title: Home
nav_order: 1
description: Fast, accurate solar irradiance data and forecasting for renewable energy applications
---

## 🚀 Solar Irradiance Forecast API

Fast, accurate solar irradiance data and forecasting for renewable energy applications.

<div class="btn-group">
  <a href="{{ '/getting-started/' | relative_url }}" class="btn btn-primary">
    <i class="fas fa-rocket"></i> Get Started
  </a>
  <a href="{{ '/api-reference/' | relative_url }}" class="btn btn-outline-primary">
    <i class="fas fa-book"></i> API Reference
  </a>
</div>

## Key Features

> **📊 Historical Data** - Access hourly historical solar irradiance, temperature, wind speed, humidity, precipitation, and cloud cover data from NASA POWER worldwide.
{: .prompt-info}

> **🔮 AI-Powered Forecasting** - Get accurate 7-day solar irradiance forecasts using machine learning models trained on weather data and solar geometry.
{: .prompt-tip}

> **🌍 Global Coverage** - Historical data available globally. Forecasting currently optimized for the Benelux region (Netherlands, Belgium, Luxembourg).
{: .prompt-note}

> **⚡ Fast & Reliable** - Built with FastAPI for high performance. RESTful JSON API with comprehensive error handling and validation.
{: .prompt-info}

> **📱 Developer Friendly** - Simple HTTP GET requests with intuitive parameter names. No authentication required for public data access.
{: .prompt-tip}

> **🔧 Production Ready** - Deployed on Render with automatic scaling. Comprehensive documentation and code examples included.
{: .prompt-note}

## 🔗 Quick Example

Get historical solar irradiance data for Amsterdam:

```bash
curl "{{ site.api_base_url }}/v1/irradiance/historical?lat={{ site.example_lat }}&lon={{ site.example_lon }}&start=20240101&end=20240102&parameters=total_irradiance"
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

**Response:**
```json
{
  "location": {"lat": 52.3676, "lon": 4.9041},
  "unit": "W/m²",
  "irradiance": {
    "2024010108": 19.42,
    "2024010109": 65.2,
    "2024010110": 128.6,
    "2024010111": 201.5
  }
}
```

## 🎯 Use Cases

<div class="row">
  <div class="col-md-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">🏠 Solar Panel Optimization</h5>
        <p class="card-text">Optimize solar panel placement and energy storage systems using historical irradiance data and accurate forecasts.</p>
      </div>
    </div>
  </div>
  <div class="col-md-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">⚡ Energy Trading</h5>
        <p class="card-text">Make informed energy trading decisions with precise solar generation forecasts for the next 7 days.</p>
      </div>
    </div>
  </div>
</div>

<div class="row mt-3">
  <div class="col-md-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">🌱 Research & Analytics</h5>
        <p class="card-text">Analyze solar potential, climate patterns, and renewable energy trends using comprehensive historical datasets.</p>
      </div>
    </div>
  </div>
  <div class="col-md-6">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">📊 Grid Management</h5>
        <p class="card-text">Predict solar energy output for better grid stability and renewable energy integration planning.</p>
      </div>
    </div>
  </div>
</div>

## 📋 Available Endpoints

| Endpoint | Purpose | Coverage |
|----------|---------|----------|
| [`/v1/irradiance/historical`]({{ '/getting-started/' | relative_url }}#historical-data) | Historical solar irradiance and weather data | Global (NASA POWER) |
| [`/v1/irradiance/forecast`]({{ '/getting-started/' | relative_url }}#forecast-data) | 7-day solar irradiance forecasts | Benelux region |

## 🌟 Why Choose Our API?

- **Accuracy**: ML models trained on extensive historical data
- **Speed**: Sub-second response times for most queries  
- **No Limits**: Free access for reasonable usage patterns
- **Support**: Comprehensive documentation and community support

## 🚀 Ready to Get Started?

<div class="text-center mt-4">
  <p class="lead">Start integrating solar irradiance data into your applications today!</p>
  <a href="{{ '/getting-started/' | relative_url }}" class="btn btn-primary btn-lg">
    <i class="fas fa-arrow-right"></i> View Documentation
  </a>
</div>

<script>
function copyToClipboard(text) {
  navigator.clipboard.writeText(text.trim()).then(function() {
    // You could add a toast notification here
    console.log('Copied to clipboard');
  });
}
</script>
