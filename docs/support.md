---
layout: page
title: Support & Community
permalink: /support/
description: Get help, report issues, and connect with the Solar Irradiance Forecast API community for technical support and collaboration.
---

## 🤝 Getting Help

We're committed to providing excellent support for developers using the Solar Irradiance Forecast API. Whether you're just getting started or building complex applications, we're here to help.

---

## 📞 Support Channels

### 🐛 Bug Reports & Feature Requests
For technical issues, bugs, or feature requests, please use our GitHub repository:

<div class="feature-card">
  <h3>GitHub Issues</h3>
  <p>Report bugs, request features, or ask technical questions through our GitHub repository.</p>
  <a href="https://github.com/oguzhansavas/solar_api/issues" class="btn btn-primary" target="_blank">
    🐛 Report an Issue
  </a>
  <a href="https://github.com/oguzhansavas/solar_api/issues/new?template=feature_request.md" class="btn btn-secondary" target="_blank">
    ✨ Request Feature
  </a>
</div>

### 💬 Community Discussions
Join our community discussions for general questions, use case sharing, and collaboration:

<div class="feature-card">
  <h3>GitHub Discussions</h3>
  <p>Connect with other developers, share your projects, and get community support.</p>
  <a href="https://github.com/oguzhansavas/solar_api/discussions" class="btn btn-primary" target="_blank">
    💬 Join Discussions
  </a>
</div>

### 📧 Direct Contact
For business inquiries, partnerships, or sensitive issues:

<div class="feature-card">
  <h3>Email Support</h3>
  <p>Reach out directly for business-related questions or private support needs.</p>
  <a href="mailto:oguzhan.savas@example.com" class="btn btn-primary">
    📧 Email Us
  </a>
</div>

---

## 🚀 Quick Self-Help

### Common Issues & Solutions

<div class="param-card">
  <h4>❌ "Invalid coordinates" Error</h4>
  <p><strong>Problem:</strong> Getting validation errors for latitude/longitude values.</p>
  <p><strong>Solution:</strong></p>
  <ul>
    <li>Ensure latitude is between -90 and 90</li>
    <li>Ensure longitude is between -180 and 180</li>
    <li>Use decimal degrees format (e.g., 52.3676, not 52°22'3.36")</li>
  </ul>
  <p><strong>Example:</strong></p>
  <pre><code># ✅ Correct
lat=52.3676&lon=4.9041

# ❌ Incorrect  
lat=92.3676&lon=4.9041  # Latitude > 90</code></pre>
</div>

<div class="param-card">
  <h4>🌍 "Forecast not available" Error</h4>
  <p><strong>Problem:</strong> Forecast endpoint returns location not supported error.</p>
  <p><strong>Solution:</strong></p>
  <ul>
    <li>Check if your coordinates are within the Benelux region</li>
    <li>Use the <a href="{{ '/coverage.html' | relative_url }}">coverage page</a> to verify location support</li>
    <li>For locations outside Benelux, use the historical endpoint instead</li>
  </ul>
  <p><strong>Coverage Check:</strong></p>
  <pre><code># Netherlands: lat 50.7-53.6, lon 3.2-7.2
# Belgium: lat 49.5-51.5, lon 2.5-6.4  
# Luxembourg: lat 49.4-50.2, lon 5.7-6.5</code></pre>
</div>

<div class="param-card">
  <h4>📅 Date Format Errors</h4>
  <p><strong>Problem:</strong> Date parameter format is incorrect.</p>
  <p><strong>Solution:</strong></p>
  <ul>
    <li>Historical endpoint: Use YYYYMMDD format (e.g., 20240101)</li>
    <li>Forecast endpoint: Use YYYYMMDDHH format (e.g., 2025070800)</li>
    <li>All dates should be in UTC timezone</li>
  </ul>
  <p><strong>Examples:</strong></p>
  <pre><code># Historical - January 1, 2024
start=20240101&end=20240102

# Forecast - July 8, 2025 at 08:00 UTC
start=2025070800&end=2025070900</code></pre>
</div>

<div class="param-card">
  <h4>⚡ Slow Response Times</h4>
  <p><strong>Problem:</strong> API requests are taking too long.</p>
  <p><strong>Solutions:</strong></p>
  <ul>
    <li>Reduce date range for large historical requests</li>
    <li>Implement request caching for frequently accessed data</li>
    <li>Use appropriate timeout values in your HTTP client</li>
    <li>Consider making parallel requests for different locations</li>
  </ul>
</div>

<div class="param-card">
  <h4>💾 Large Data Responses</h4>
  <p><strong>Problem:</strong> Response size is larger than expected.</p>
  <p><strong>Solutions:</strong></p>
  <ul>
    <li>Request smaller date ranges and combine client-side</li>
    <li>Use compression in your HTTP client (gzip)</li>
    <li>Process data as streams rather than loading entirely into memory</li>
  </ul>
</div>

---

## 📖 Documentation & Resources

### 📚 Developer Resources

| Resource | Description | Link |
|----------|-------------|------|
| **Getting Started** | Quick start guide with basic examples | [View Guide]({{ '/getting-started.html' | relative_url }}) |
| **API Reference** | Complete endpoint documentation | [View Reference]({{ '/api-reference.html' | relative_url }}) |
| **Examples** | Real-world use cases and code samples | [View Examples]({{ '/examples.html' | relative_url }}) |
| **Coverage Info** | Geographic coverage and limitations | [View Coverage]({{ '/coverage.html' | relative_url }}) |

### 🔧 Development Tools

```bash
# Health check endpoint
curl "{{ site.api_base_url }}/health"

# OpenAPI specification
curl "{{ site.api_base_url }}/openapi.json"

# Interactive API docs
# Visit: {{ site.api_base_url }}/docs
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

### 📊 Service Status

Check current API status and performance:

- **API Health**: [{{ site.api_base_url }}/health]({{ site.api_base_url }}/health)
- **Response Times**: Typically 100-500ms for historical, 200-800ms for forecast
- **Uptime Target**: 99.9% availability
- **Rate Limits**: No strict limits for reasonable usage

---

## 🔍 Troubleshooting Guide

### Debug Your API Calls

Use this debugging checklist to troubleshoot issues:

```python
import requests
import json
from datetime import datetime

def debug_api_call(endpoint, params):
    """Debug API calls with detailed error information"""
    
    print(f"🔍 Debugging API call to {endpoint}")
    print(f"📋 Parameters: {params}")
    
    # Validate parameters before sending
    validation_errors = validate_params(endpoint, params)
    if validation_errors:
        print(f"❌ Parameter validation errors:")
        for error in validation_errors:
            print(f"   - {error}")
        return None
    
    try:
        # Make the request
        print(f"🌐 Sending request...")
        response = requests.get(endpoint, params=params, timeout=30)
        
        print(f"📈 Response status: {response.status_code}")
        print(f"⏱️  Response time: {response.elapsed.total_seconds():.2f}s")
        print(f"📏 Response size: {len(response.content)} bytes")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success! Got {len(data.get('irradiance', data.get('forecast', {})))} data points")
            return data
        else:
            print(f"❌ Error response:")
            try:
                error_data = response.json()
                print(f"   Detail: {error_data.get('detail', 'Unknown error')}")
            except:
                print(f"   Raw response: {response.text}")
            return None
            
    except requests.exceptions.Timeout:
        print("⏰ Request timed out (>30s)")
    except requests.exceptions.ConnectionError:
        print("🔌 Connection error - check internet connection")
    except requests.exceptions.RequestException as e:
        print(f"🚫 Request failed: {e}")
    except json.JSONDecodeError:
        print("📄 Invalid JSON response")
    
    return None

def validate_params(endpoint, params):
    """Validate parameters before sending request"""
    errors = []
    
    # Check required parameters
    if 'lat' not in params or 'lon' not in params:
        errors.append("Missing required lat/lon parameters")
    
    # Validate coordinates
    try:
        lat, lon = float(params['lat']), float(params['lon'])
        if not (-90 <= lat <= 90):
            errors.append(f"Invalid latitude: {lat} (must be -90 to 90)")
        if not (-180 <= lon <= 180):
            errors.append(f"Invalid longitude: {lon} (must be -180 to 180)")
    except (ValueError, KeyError):
        errors.append("Latitude/longitude must be valid numbers")
    
    # Endpoint-specific validation
    if 'historical' in endpoint:
        if 'start' not in params or 'end' not in params:
            errors.append("Historical endpoint requires start and end dates")
        if 'parameters' not in params:
            errors.append("Historical endpoint requires parameters field")
    
    elif 'forecast' in endpoint:
        if 'start' not in params or 'end' not in params:
            errors.append("Forecast endpoint requires start and end datetimes")
        # Check if location is in Benelux
        try:
            lat, lon = float(params['lat']), float(params['lon'])
            if not is_benelux_region(lat, lon):
                errors.append("Forecast endpoint only supports Benelux region")
        except:
            pass
    
    return errors

def is_benelux_region(lat, lon):
    """Check if coordinates are in Benelux region"""
    benelux_bounds = [
        (50.7, 53.6, 3.2, 7.2),  # Netherlands
        (49.5, 51.5, 2.5, 6.4),  # Belgium  
        (49.4, 50.2, 5.7, 6.5)   # Luxembourg
    ]
    
    for lat_min, lat_max, lon_min, lon_max in benelux_bounds:
        if lat_min <= lat <= lat_max and lon_min <= lon <= lon_max:
            return True
    return False

# Example usage
params = {
    'lat': {{ site.example_lat }},
    'lon': {{ site.example_lon }},
    'start': '20240101',
    'end': '20240102',
    'parameters': 'total_irradiance'
}

result = debug_api_call("{{ site.api_base_url }}/v1/irradiance/historical", params)
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

---

## 🌟 Contributing

### How to Contribute

We welcome contributions from the community! Here's how you can help:

<div class="use-cases">
  <div class="use-case">
    <h4>📝 Documentation</h4>
    <p>Help improve our documentation, add examples, or translate content to other languages.</p>
  </div>
  
  <div class="use-case">
    <h4>🐛 Bug Reports</h4>
    <p>Report bugs with detailed reproduction steps and expected vs actual behavior.</p>
  </div>
  
  <div class="use-case">
    <h4>💡 Feature Ideas</h4>
    <p>Suggest new features, endpoints, or improvements based on your use cases.</p>
  </div>
  
  <div class="use-case">
    <h4>🧪 Testing</h4>
    <p>Help test new features, validate accuracy in different regions, or performance testing.</p>
  </div>
</div>

### Contribution Guidelines

1. **Check existing issues** before creating new ones
2. **Provide detailed information** including error messages, request/response examples
3. **Use clear, descriptive titles** for issues and PRs
4. **Follow the code of conduct** and be respectful to all community members

---

## 📋 Issue Templates

### Bug Report Template

When reporting bugs, please include:

```markdown
## Bug Description
Brief description of the issue

## Steps to Reproduce
1. Step one
2. Step two
3. Step three

## Expected Behavior
What you expected to happen

## Actual Behavior
What actually happened

## Request Details
- Endpoint: /v1/irradiance/historical
- Parameters: lat=52.3676&lon=4.9041&start=20240101...
- Response status: 400
- Error message: "..."

## Environment
- Programming language: Python 3.9
- HTTP client: requests 2.28.0
- Timestamp: 2024-01-15 14:30 UTC
```

### Feature Request Template

```markdown
## Feature Summary
Brief description of the proposed feature

## Use Case
Describe your specific use case and why this feature is needed

## Proposed Implementation
How you envision this feature working

## Alternative Solutions
Any alternative approaches you've considered

## Additional Context
Any other relevant information, mockups, or examples
```

---

## 🏆 Success Stories

### Community Projects

Share your project with the community! We love to see how developers are using the API:

- **Solar farm monitoring dashboards**
- **Energy trading optimization systems**
- **Academic research projects**
- **Mobile applications**
- **IoT integration projects**

### Get Featured

If you've built something interesting with our API, we'd love to feature it:

1. Share your project in [GitHub Discussions](https://github.com/oguzhansavas/solar_api/discussions)
2. Include screenshots, code samples, or demo links
3. Describe your use case and how the API helped
4. We'll feature outstanding projects in our documentation!

---

## 📈 Service Level Agreement

### Availability
- **Uptime Target**: 99.9% (less than 8.77 hours downtime per year)
- **Maintenance Windows**: Announced 48 hours in advance
- **Status Updates**: Real-time status at [{{ site.api_base_url }}/health]({{ site.api_base_url }}/health)

### Response Times
- **Historical Endpoint**: Target 95th percentile < 1 second
- **Forecast Endpoint**: Target 95th percentile < 2 seconds
- **Health Check**: Target 95th percentile < 100ms

### Support Response Times
- **Critical Issues**: 4 hours
- **Bug Reports**: 24 hours
- **Feature Requests**: 72 hours
- **General Questions**: 48 hours

---

## 💝 Acknowledgments

### Data Sources
- **NASA POWER**: Global historical solar and meteorological data
- **Open-Meteo**: Weather forecast data for ML model inputs
- **pvlib**: Solar position and irradiance calculations

### Community
Special thanks to all contributors, beta testers, and community members who help improve the API through feedback and contributions.

<script>
function copyToClipboard(text) {
  navigator.clipboard.writeText(text.trim()).then(function() {
    console.log('Copied to clipboard');
  });
}
</script>