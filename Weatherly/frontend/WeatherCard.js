import React from "react";

function WeatherCard({ data }) {
  return (
    <div className="card">
      <h2>{data.city}</h2>
      <p>Temperature: {data.temp_c}°C / {data.temp_f}°F</p>
      <p>Condition: {data.condition}</p>
    </div>
  );
}

export default WeatherCard;