import json
import os
from temp_converter import celsius_to_fahrenheit
from cache import get_from_cache, add_to_cache

def get_weather_data(city):    
    """Fetch weather data from local JSON."""
    cached = get_from_cache(city)
    if cached:
        return cached
    try:
        path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_weather.json')
        with open(path, 'r') as f:
            data = json.load(f)
        city_data = data.get(city)
        if not city_data:
            return {"error": "City not found"}
        city_data["temp_f"] = celsius_to_fahrenheit(city_data["temp_c"])
        add_to_cache(city, city_data)
        return city_data
    except Exception as e:
        return {"error": str(e)}

