---
layout: page
title: Examples & Use Cases
icon: fas fa-code
order: 3
permalink: /examples/
description: Real-world examples and practical use cases for the Solar Irradiance Forecast API with code samples in multiple languages.
toc: true
---

## 🎯 Real-World Use Cases

Explore practical applications and implementation examples for the Solar Irradiance Forecast API.

---

## 🏠 Solar Panel Optimization

Optimize solar panel placement and energy storage systems using historical irradiance data.

### Use Case: Annual Solar Potential Analysis

Calculate the annual solar energy potential for a rooftop installation in Amsterdam:

```python
import requests
import pandas as pd
from datetime import datetime, timedelta

def calculate_annual_solar_potential(lat, lon, year=2023):
    """Calculate annual solar potential for a given location"""
    
    # Get historical data for the entire year
    start_date = f"{year}0101"
    end_date = f"{year}1231"
    
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
    data = response.json()
    
    # Convert to DataFrame for analysis
    irradiance_data = data['irradiance']
    df = pd.DataFrame(list(irradiance_data.items()), 
                     columns=['timestamp', 'irradiance'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y%m%d%H')
    df['irradiance'] = pd.to_numeric(df['irradiance'])
    
    # Calculate daily totals (Wh/m²)
    df['date'] = df['timestamp'].dt.date
    daily_totals = df.groupby('date')['irradiance'].sum()
    
    # Annual statistics
    annual_total = daily_totals.sum()  # Wh/m²/year
    peak_day = daily_totals.max()      # Wh/m²/day
    average_daily = daily_totals.mean() # Wh/m²/day
    
    return {
        'annual_total_kwh_m2': annual_total / 1000,
        'peak_day_kwh_m2': peak_day / 1000,
        'average_daily_kwh_m2': average_daily / 1000,
        'location': f"({lat}, {lon})"
    }

# Example usage for Amsterdam
result = calculate_annual_solar_potential({{ site.example_lat }}, {{ site.example_lon }})
print(f"Annual Solar Potential Analysis for {result['location']}:")
print(f"Annual Total: {result['annual_total_kwh_m2']:.1f} kWh/m²")
print(f"Peak Day: {result['peak_day_kwh_m2']:.1f} kWh/m²")
print(f"Daily Average: {result['average_daily_kwh_m2']:.1f} kWh/m²")
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

---

## ⚡ Energy Trading & Grid Management

Make informed energy trading decisions with precise solar generation forecasts.

### Use Case: 7-Day Power Production Forecast

Forecast solar power output for energy trading decisions:

```javascript
class SolarForecastTrader {
    constructor(apiBaseUrl, lat, lon, systemCapacity) {
        this.apiBaseUrl = apiBaseUrl;
        this.lat = lat;
        this.lon = lon;
        this.systemCapacity = systemCapacity; // kW
    }

    async getForecastData(startDate, endDate) {
        const url = `${this.apiBaseUrl}/v1/irradiance/forecast`;
        const params = new URLSearchParams({
            lat: this.lat,
            lon: this.lon,
            start: startDate,
            end: endDate
        });

        try {
            const response = await fetch(`${url}?${params}`);
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching forecast:', error);
            return null;
        }
    }

    calculatePowerOutput(irradiance) {
        // Convert irradiance (W/m²) to power output (kW)
        // Assumes standard panel efficiency and array size
        const panelEfficiency = 0.20; // 20% efficiency
        const arrayArea = this.systemCapacity / 0.25; // m² (assuming 250W/m²)
        
        return (irradiance * arrayArea * panelEfficiency) / 1000; // kW
    }

    async generateTradingStrategy(days = 7) {
        const startDate = new Date();
        const endDate = new Date(startDate);
        endDate.setDate(endDate.getDate() + days);

        const startStr = this.formatDateTime(startDate);
        const endStr = this.formatDateTime(endDate);

        const forecast = await this.getForecastData(startStr, endStr);
        
        if (!forecast) return null;

        const strategy = {
            totalForecastMWh: 0,
            dailyBreakdown: [],
            recommendations: []
        };

        // Process hourly forecasts
        const hourlyData = Object.entries(forecast.forecast);
        const dailyTotals = {};

        for (const [timestamp, irradiance] of hourlyData) {
            const date = timestamp.split(' ')[0];
            const powerKW = this.calculatePowerOutput(irradiance);
            
            if (!dailyTotals[date]) {
                dailyTotals[date] = { totalMWh: 0, peakKW: 0, hours: [] };
            }
            
            dailyTotals[date].totalMWh += powerKW / 1000; // Convert to MWh
            dailyTotals[date].peakKW = Math.max(dailyTotals[date].peakKW, powerKW);
            dailyTotals[date].hours.push({ timestamp, irradiance, powerKW });
        }

        // Generate recommendations
        for (const [date, data] of Object.entries(dailyTotals)) {
            strategy.dailyBreakdown.push({
                date: date,
                totalMWh: data.totalMWh.toFixed(2),
                peakKW: data.peakKW.toFixed(2)
            });

            strategy.totalForecastMWh += data.totalMWh;

            // Trading recommendations
            if (data.totalMWh > 50) {
                strategy.recommendations.push(`${date}: High production day - Consider selling excess energy`);
            } else if (data.totalMWh < 20) {
                strategy.recommendations.push(`${date}: Low production day - Consider purchasing backup energy`);
            }
        }

        return strategy;
    }

    formatDateTime(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        const hour = String(date.getHours()).padStart(2, '0');
        return `${year}${month}${day}${hour}`;
    }
}

// Example usage
const trader = new SolarForecastTrader(
    "{{ site.api_base_url }}", 
    {{ site.example_lat }}, 
    {{ site.example_lon }}, 
    100 // 100kW system
);

trader.generateTradingStrategy(7).then(strategy => {
    if (strategy) {
        console.log('7-Day Solar Trading Strategy:');
        console.log(`Total Forecast: ${strategy.totalForecastMWh.toFixed(2)} MWh`);
        console.log('Daily Breakdown:', strategy.dailyBreakdown);
        console.log('Recommendations:', strategy.recommendations);
    }
});
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

---

## 📊 Research & Analytics

Analyze solar potential and climate patterns using comprehensive historical datasets.

### Use Case: Seasonal Pattern Analysis

Analyze seasonal solar irradiance patterns for climate research:

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class SolarPatternAnalyzer:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url
    
    def get_multi_year_data(self, lat, lon, start_year, end_year):
        """Fetch multiple years of historical data"""
        all_data = {}
        
        for year in range(start_year, end_year + 1):
            start_date = f"{year}0101"
            end_date = f"{year}1231"
            
            params = {
                "lat": lat,
                "lon": lon,
                "start": start_date,
                "end": end_date,
                "parameters": "total_irradiance",
                "community": "SB"
            }
            
            response = requests.get(f"{self.api_base_url}/v1/irradiance/historical", params=params)
            
            if response.status_code == 200:
                data = response.json()
                all_data[year] = data['irradiance']
            else:
                print(f"Failed to fetch data for {year}")
        
        return all_data
    
    def analyze_seasonal_patterns(self, lat, lon, years_range=(2020, 2023)):
        """Analyze seasonal patterns across multiple years"""
        start_year, end_year = years_range
        raw_data = self.get_multi_year_data(lat, lon, start_year, end_year)
        
        # Convert to DataFrame
        all_records = []
        for year, year_data in raw_data.items():
            for timestamp, irradiance in year_data.items():
                dt = datetime.strptime(timestamp, '%Y%m%d%H')
                all_records.append({
                    'datetime': dt,
                    'year': dt.year,
                    'month': dt.month,
                    'hour': dt.hour,
                    'day_of_year': dt.timetuple().tm_yday,
                    'irradiance': float(irradiance)
                })
        
        df = pd.DataFrame(all_records)
        
        # Seasonal analysis
        monthly_avg = df.groupby('month')['irradiance'].mean()
        hourly_avg = df.groupby('hour')['irradiance'].mean()
        
        # Daily totals by month
        df['date'] = df['datetime'].dt.date
        daily_totals = df.groupby(['date', 'month'])['irradiance'].sum().reset_index()
        monthly_daily_avg = daily_totals.groupby('month')['irradiance'].mean()
        
        return {
            'monthly_hourly_avg': monthly_avg,
            'hourly_pattern': hourly_avg,
            'monthly_daily_totals': monthly_daily_avg,
            'dataframe': df
        }
    
    def generate_insights(self, analysis_results, location_name):
        """Generate insights from the analysis"""
        monthly_avg = analysis_results['monthly_hourly_avg']
        hourly_avg = analysis_results['hourly_pattern']
        monthly_totals = analysis_results['monthly_daily_totals']
        
        insights = {
            'location': location_name,
            'peak_month': monthly_avg.idxmax(),
            'peak_month_avg': monthly_avg.max(),
            'lowest_month': monthly_avg.idxmin(),
            'lowest_month_avg': monthly_avg.min(),
            'peak_hour': hourly_avg.idxmax(),
            'peak_hour_avg': hourly_avg.max(),
            'summer_vs_winter_ratio': monthly_avg[6] / monthly_avg[12],  # June vs December
            'best_daily_total_month': monthly_totals.idxmax(),
            'best_daily_total': monthly_totals.max()
        }
        
        return insights

# Example usage
analyzer = SolarPatternAnalyzer("{{ site.api_base_url }}")

# Analyze Amsterdam's solar patterns
results = analyzer.analyze_seasonal_patterns({{ site.example_lat }}, {{ site.example_lon }}, (2021, 2023))
insights = analyzer.generate_insights(results, "{{ site.example_location }}")

print(f"Solar Pattern Analysis for {insights['location']}:")
print(f"Peak Month: {insights['peak_month']} ({insights['peak_month_avg']:.1f} W/m² avg)")
print(f"Lowest Month: {insights['lowest_month']} ({insights['lowest_month_avg']:.1f} W/m² avg)")
print(f"Peak Hour: {insights['peak_hour']:02d}:00 ({insights['peak_hour_avg']:.1f} W/m² avg)")
print(f"Summer/Winter Ratio: {insights['summer_vs_winter_ratio']:.1f}x")
print(f"Best Month for Daily Total: {insights['best_daily_total_month']} ({insights['best_daily_total']:.0f} Wh/m²/day avg)")
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

---

## 🌤️ Weather Correlation Analysis

Analyze the relationship between weather conditions and solar irradiance.

### Use Case: Cloud Cover Impact Study

Study how cloud cover affects solar irradiance:

```bash
# Multi-parameter analysis - Cloud cover vs Solar irradiance
curl "{{ site.api_base_url }}/v1/irradiance/historical?lat={{ site.example_lat }}&lon={{ site.example_lon }}&start=20240601&end=20240630&parameters=total_irradiance" > irradiance_june.json

curl "{{ site.api_base_url }}/v1/irradiance/historical?lat={{ site.example_lat }}&lon={{ site.example_lon }}&start=20240601&end=20240630&parameters=cloud_cover" > clouds_june.json
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

```python
import json
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Load both datasets
with open('irradiance_june.json', 'r') as f:
    irradiance_data = json.load(f)

with open('clouds_june.json', 'r') as f:
    cloud_data = json.load(f)

# Create correlation analysis
timestamps = list(irradiance_data['irradiance'].keys())
irradiance_values = [irradiance_data['irradiance'][ts] for ts in timestamps]
cloud_values = [cloud_data['irradiance'][ts] for ts in timestamps]  # Note: response uses 'irradiance' key

# Filter daytime hours only (06:00 to 18:00)
daytime_data = []
for i, ts in enumerate(timestamps):
    hour = int(ts[-2:])
    if 6 <= hour <= 18:
        daytime_data.append({
            'timestamp': ts,
            'irradiance': irradiance_values[i],
            'cloud_cover': cloud_values[i]
        })

df = pd.DataFrame(daytime_data)
df['irradiance'] = pd.to_numeric(df['irradiance'])
df['cloud_cover'] = pd.to_numeric(df['cloud_cover'])

# Calculate correlation
correlation, p_value = pearsonr(df['cloud_cover'], df['irradiance'])

print(f"Cloud Cover vs Solar Irradiance Analysis:")
print(f"Correlation coefficient: {correlation:.3f}")
print(f"P-value: {p_value:.6f}")
print(f"Relationship: {'Strong' if abs(correlation) > 0.7 else 'Moderate' if abs(correlation) > 0.4 else 'Weak'}")

# Efficiency analysis by cloud cover bins
df['cloud_bin'] = pd.cut(df['cloud_cover'], bins=[0, 25, 50, 75, 100], labels=['Clear', 'Partly Cloudy', 'Mostly Cloudy', 'Overcast'])
efficiency_by_clouds = df.groupby('cloud_bin')['irradiance'].agg(['mean', 'std', 'count'])

print("\nIrradiance by Cloud Cover Category:")
for category in efficiency_by_clouds.index:
    mean_irr = efficiency_by_clouds.loc[category, 'mean']
    std_irr = efficiency_by_clouds.loc[category, 'std']
    count = efficiency_by_clouds.loc[category, 'count']
    print(f"{category}: {mean_irr:.1f} ± {std_irr:.1f} W/m² (n={count})")
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

---

## 🔄 Real-Time Monitoring Dashboard

Build a real-time monitoring system combining historical data with forecasts.

### Use Case: Solar Farm Monitoring

Create a monitoring dashboard for solar farm operators:

```javascript
class SolarFarmDashboard {
    constructor(apiBaseUrl, farmConfig) {
        this.apiBaseUrl = apiBaseUrl;
        this.farmConfig = farmConfig; // {lat, lon, capacity, efficiency}
        this.updateInterval = 1000 * 60 * 15; // 15 minutes
    }

    async getCurrentStatus() {
        // Get yesterday's actual performance
        const yesterday = new Date();
        yesterday.setDate(yesterday.getDate() - 1);
        const yesterdayStr = this.formatDate(yesterday);

        // Get today's forecast
        const today = new Date();
        const todayStart = this.formatDateTime(today);
        const tomorrow = new Date(today);
        tomorrow.setDate(tomorrow.getDate() + 1);
        const tomorrowStr = this.formatDateTime(tomorrow);

        try {
            const [historical, forecast] = await Promise.all([
                this.getHistoricalData(yesterdayStr, yesterdayStr),
                this.getForecastData(todayStart, tomorrowStr)
            ]);

            return this.processStatus(historical, forecast);
        } catch (error) {
            console.error('Error fetching status:', error);
            return null;
        }
    }

    async getHistoricalData(startDate, endDate) {
        const url = `${this.apiBaseUrl}/v1/irradiance/historical`;
        const params = new URLSearchParams({
            lat: this.farmConfig.lat,
            lon: this.farmConfig.lon,
            start: startDate,
            end: endDate,
            parameters: 'total_irradiance'
        });

        const response = await fetch(`${url}?${params}`);
        return response.json();
    }

    async getForecastData(startDateTime, endDateTime) {
        const url = `${this.apiBaseUrl}/v1/irradiance/forecast`;
        const params = new URLSearchParams({
            lat: this.farmConfig.lat,
            lon: this.farmConfig.lon,
            start: startDateTime,
            end: endDateTime
        });

        const response = await fetch(`${url}?${params}`);
        return response.json();
    }

    processStatus(historical, forecast) {
        // Calculate yesterday's performance
        const yesterdayIrradiance = Object.values(historical.irradiance).map(Number);
        const yesterdayTotal = yesterdayIrradiance.reduce((sum, val) => sum + val, 0);
        const yesterdayPowerMWh = this.irradianceToPower(yesterdayTotal) / 1000;

        // Process today's forecast
        const todayForecast = Object.entries(forecast.forecast);
        const todayTotal = todayForecast.reduce((sum, [_, irr]) => sum + irr, 0);
        const todayForecastMWh = this.irradianceToPower(todayTotal) / 1000;

        // Find peak hours
        const peakHour = todayForecast.reduce((max, [time, irr]) => 
            irr > max.irr ? {time, irr} : max, {time: '', irr: 0});

        return {
            timestamp: new Date().toISOString(),
            yesterday: {
                totalMWh: yesterdayPowerMWh.toFixed(2),
                avgIrradiance: (yesterdayTotal / yesterdayIrradiance.length).toFixed(1)
            },
            today: {
                forecastMWh: todayForecastMWh.toFixed(2),
                peakHour: peakHour.time,
                peakIrradiance: peakHour.irr.toFixed(1)
            },
            farmCapacity: this.farmConfig.capacity,
            efficiency: this.farmConfig.efficiency
        };
    }

    irradianceToPower(irradiance) {
        // Convert total irradiance (Wh/m²) to power (kWh)
        return irradiance * this.farmConfig.capacity * this.farmConfig.efficiency / 1000;
    }

    formatDate(date) {
        const year = date.getFullYear();
        const month = String(date.getMonth() + 1).padStart(2, '0');
        const day = String(date.getDate()).padStart(2, '0');
        return `${year}${month}${day}`;
    }

    formatDateTime(date) {
        return this.formatDate(date) + String(date.getHours()).padStart(2, '0');
    }

    startMonitoring() {
        console.log('Starting solar farm monitoring...');
        
        const updateDashboard = async () => {
            const status = await this.getCurrentStatus();
            if (status) {
                this.displayStatus(status);
            }
        };

        // Initial update
        updateDashboard();
        
        // Set up periodic updates
        setInterval(updateDashboard, this.updateInterval);
    }

    displayStatus(status) {
        console.clear();
        console.log('=== SOLAR FARM DASHBOARD ===');
        console.log(`Last Update: ${new Date(status.timestamp).toLocaleString()}`);
        console.log('');
        console.log('Yesterday Performance:');
        console.log(`  Total Energy: ${status.yesterday.totalMWh} MWh`);
        console.log(`  Avg Irradiance: ${status.yesterday.avgIrradiance} W/m²`);
        console.log('');
        console.log('Today Forecast:');
        console.log(`  Forecast Energy: ${status.today.forecastMWh} MWh`);
        console.log(`  Peak Hour: ${status.today.peakHour}`);
        console.log(`  Peak Irradiance: ${status.today.peakIrradiance} W/m²`);
        console.log('');
        console.log(`Farm Capacity: ${status.farmCapacity} MW`);
        console.log(`Efficiency: ${(status.efficiency * 100).toFixed(1)}%`);
    }
}

// Example usage
const farmConfig = {
    lat: {{ site.example_lat }},
    lon: {{ site.example_lon }},
    capacity: 50, // 50 MW solar farm
    efficiency: 0.18 // 18% panel efficiency
};

const dashboard = new SolarFarmDashboard("{{ site.api_base_url }}", farmConfig);
dashboard.startMonitoring();
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

---

## 📱 Integration Examples

### Webhook Integration for Alerts

Set up automated alerts based on forecast conditions:

```python
import requests
import schedule
import time
from datetime import datetime, timedelta

class SolarAlertSystem:
    def __init__(self, api_base_url, webhook_url, locations):
        self.api_base_url = api_base_url
        self.webhook_url = webhook_url
        self.locations = locations
    
    def check_weather_alerts(self):
        """Check for significant weather events affecting solar production"""
        tomorrow = datetime.now() + timedelta(days=1)
        start = tomorrow.strftime('%Y%m%d00')
        end = tomorrow.strftime('%Y%m%d23')
        
        for location in self.locations:
            try:
                # Get forecast for tomorrow
                params = {
                    'lat': location['lat'],
                    'lon': location['lon'],
                    'start': start,
                    'end': end
                }
                
                response = requests.get(f"{self.api_base_url}/v1/irradiance/forecast", params=params)
                data = response.json()
                
                # Analyze forecast
                hourly_values = list(data['forecast'].values())
                daily_total = sum(hourly_values)
                peak_hour = max(hourly_values)
                
                # Generate alerts
                alerts = []
                
                if daily_total < 1000:  # Less than 1 kWh/m²
                    alerts.append({
                        'type': 'LOW_PRODUCTION',
                        'message': f'Low solar production forecast for {location["name"]}: {daily_total:.0f} Wh/m²',
                        'severity': 'warning'
                    })
                
                if peak_hour > 800:  # Very high peak
                    alerts.append({
                        'type': 'HIGH_PRODUCTION',
                        'message': f'High solar production forecast for {location["name"]}: peak {peak_hour:.0f} W/m²',
                        'severity': 'info'
                    })
                
                # Send alerts
                for alert in alerts:
                    self.send_alert(alert, location)
                    
            except Exception as e:
                print(f"Error checking alerts for {location['name']}: {e}")
    
    def send_alert(self, alert, location):
        """Send alert to webhook"""
        payload = {
            'text': f"🌞 Solar Alert: {alert['message']}",
            'location': location['name'],
            'coordinates': f"({location['lat']}, {location['lon']})",
            'severity': alert['severity'],
            'timestamp': datetime.now().isoformat()
        }
        
        try:
            requests.post(self.webhook_url, json=payload)
            print(f"Alert sent for {location['name']}: {alert['message']}")
        except Exception as e:
            print(f"Failed to send alert: {e}")

# Example usage
locations = [
    {'name': 'Amsterdam Solar Farm', 'lat': {{ site.example_lat }}, 'lon': {{ site.example_lon }}},
    {'name': 'Rotterdam Installation', 'lat': 51.9244, 'lon': 4.4777}
]

alert_system = SolarAlertSystem(
    "{{ site.api_base_url }}", 
    "https://hooks.slack.com/your-webhook-url",
    locations
)

# Schedule daily checks
schedule.every().day.at("18:00").do(alert_system.check_weather_alerts)

# Run scheduler
while True:
    schedule.run_pending()
    time.sleep(60)
```

<button class="copy-btn" onclick="copyToClipboard(this.previousElementSibling.textContent)">📋 Copy</button>

---

## 🔧 Best Practices & Tips

### Error Handling & Retry Logic

```python
import time
import random
from functools import wraps

def retry_with_backoff(retries=3, backoff_in_seconds=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x = 0
            while x <= retries:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    if x == retries:
                        raise e
                    sleep_time = (backoff_in_seconds * 2 ** x + 
                                random.uniform(0, 1))
                    time.sleep(sleep_time)
                    x += 1
        return wrapper
    return decorator

@retry_with_backoff(retries=3, backoff_in_seconds=2)
def robust_api_call(url, params):
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()
```

### Data Caching Strategy

```python
import json
import os
from datetime import datetime, timedelta

class APICache:
    def __init__(self, cache_dir='cache'):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)
    
    def get_cache_key(self, params):
        return f"{params['lat']}_{params['lon']}_{params['start']}_{params['end']}.json"
    
    def is_cache_valid(self, file_path, max_age_hours=24):
        if not os.path.exists(file_path):
            return False
        
        file_age = datetime.now() - datetime.fromtimestamp(os.path.getmtime(file_path))
        return file_age < timedelta(hours=max_age_hours)
    
    def get_cached_data(self, params):
        cache_file = os.path.join(self.cache_dir, self.get_cache_key(params))
        
        if self.is_cache_valid(cache_file):
            with open(cache_file, 'r') as f:
                return json.load(f)
        return None
    
    def cache_data(self, params, data):
        cache_file = os.path.join(self.cache_dir, self.get_cache_key(params))
        with open(cache_file, 'w') as f:
            json.dump(data, f)
```

<script>
function copyToClipboard(text) {
  navigator.clipboard.writeText(text.trim()).then(function() {
    console.log('Copied to clipboard');
  });
}
</script>