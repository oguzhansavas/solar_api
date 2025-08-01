---
layout: default
title: Solar Irradiance Forecast API
description: Fast, accurate solar irradiance data and forecasting for renewable energy applications
---

<div class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">☀️ Solar Irradiance Forecast API</h1>
    <p class="hero-description">Fast, accurate solar irradiance data and forecasting for renewable energy applications</p>
    <div class="hero-buttons">
      <a href="{{ '/getting-started.html' | relative_url }}" class="btn btn-primary">Get Started</a>
      <a href="{{ '/api-reference.html' | relative_url }}" class="btn btn-secondary">API Reference</a>
    </div>
  </div>
</div>

## 🚀 Key Features

<div class="features-grid">
  <div class="feature-card">
    <h3>📊 Historical Data</h3>
    <p>Access hourly historical solar irradiance, temperature, wind speed, humidity, precipitation, and cloud cover data from NASA POWER worldwide.</p>
  </div>
  
  <div class="feature-card">
    <h3>🔮 AI-Powered Forecasting</h3>
    <p>Get accurate 7-day solar irradiance forecasts using machine learning models trained on weather data and solar geometry.</p>
  </div>
  
  <div class="feature-card">
    <h3>🌍 Global Coverage</h3>
    <p>Historical data available globally. Forecasting currently optimized for the Benelux region (Netherlands, Belgium, Luxembourg).</p>
  </div>
  
  <div class="feature-card">
    <h3>⚡ Fast & Reliable</h3>
    <p>Built with FastAPI for high performance. RESTful JSON API with comprehensive error handling and validation.</p>
  </div>
  
  <div class="feature-card">
    <h3>📱 Developer Friendly</h3>
    <p>Simple HTTP GET requests with intuitive parameter names. No authentication required for public data access.</p>
  </div>
  
  <div class="feature-card">
    <h3>🔧 Production Ready</h3>
    <p>Deployed on Render with automatic scaling. Comprehensive documentation and code examples included.</p>
  </div>
</div>

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

<div class="use-cases">
  <div class="use-case">
    <h4>🏠 Solar Panel Optimization</h4>
    <p>Optimize solar panel placement and energy storage systems using historical irradiance data and accurate forecasts.</p>
  </div>
  
  <div class="use-case">
    <h4>⚡ Energy Trading</h4>
    <p>Make informed energy trading decisions with precise solar generation forecasts for the next 7 days.</p>
  </div>
  
  <div class="use-case">
    <h4>🌱 Research & Analytics</h4>
    <p>Analyze solar potential, climate patterns, and renewable energy trends using comprehensive historical datasets.</p>
  </div>
  
  <div class="use-case">
    <h4>📊 Grid Management</h4>
    <p>Predict solar energy output for better grid stability and renewable energy integration planning.</p>
  </div>
</div>

## 📋 Available Endpoints

| Endpoint | Purpose | Coverage |
|----------|---------|----------|
| [`/v1/irradiance/historical`]({{ '/api-reference.html#historical' | relative_url }}) | Historical solar irradiance and weather data | Global (NASA POWER) |
| [`/v1/irradiance/forecast`]({{ '/api-reference.html#forecast' | relative_url }}) | 7-day solar irradiance forecasts | Benelux region |

## 🌟 Why Choose Our API?

- **Accuracy**: ML models trained on extensive historical data
- **Speed**: Sub-second response times for most queries
- **No Limits**: Free access for reasonable usage patterns
- **Support**: Comprehensive documentation and community support

## 🚀 Ready to Get Started?

<div class="cta-section">
  <p>Start integrating solar irradiance data into your applications today!</p>
  <a href="{{ '/getting-started.html' | relative_url }}" class="btn btn-large">View Documentation →</a>
</div>

<script>
function copyToClipboard(text) {
  navigator.clipboard.writeText(text.trim()).then(function() {
    // You could add a toast notification here
    console.log('Copied to clipboard');
  });
}
</script>
