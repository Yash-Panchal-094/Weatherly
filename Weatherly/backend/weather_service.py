import json
import os
from temp_converter import celsius_to_fahrenheit

def get_weather_data(city):
    """Fetch weather data from local JSON."""
    try:
        path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_weather.json')
        with open(path, 'r') as f:
            data = json.load(f)
        city_data = data.get(city)
        if not city_data:
            return {"error": "City not found"}
        city_data["temp_f"] = celsius_to_fahrenheit(city_data["temp_c"])
        return city_data
    except Exception as e:
        import traceback
        print("Error fetching weather:", traceback.format_exc())
        return {"error": "Internal server error. Please try again later."}

