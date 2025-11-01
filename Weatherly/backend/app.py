### **📂 backend/app.py**

from flask import Flask, jsonify, request
from weather_service import get_weather_data

app = Flask(__name__)

@app.route('/api/weather', methods=['GET'])
def weather():
    city = request.args.get('city', 'London')
    data = get_weather_data(city)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
