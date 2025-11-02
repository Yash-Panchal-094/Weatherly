### **📂 backend/app.py**

from flask import Flask, jsonify, request
from weather_service import get_weather_data
import random

app = Flask(__name__)

@app.route('/api/weather', methods=['GET'])
def weather():
    city = request.args.get('city', 'London')
    data = get_weather_data(city)
    return jsonify(data)

@app.route('/api/forecast', methods=['GET'])
def forecast():
    city = request.args.get('city', 'London')
    days = []
    for i in range(7):
        days.append({
            "day": f"Day {i+1}",
            "temp_c": random.randint(10, 30),
            "condition": random.choice(["Sunny", "Cloudy", "Rainy"])
        })
    return jsonify({"city": city, "forecast": days})


if __name__ == '__main__':
    app.run(debug=True)

