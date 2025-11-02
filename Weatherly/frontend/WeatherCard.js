import React from "react";

function WeatherCard({ data }) {
  if (data.error) return <p>{data.error}</p>;
  return (
    <div className="card">
      <h2>{data.city || "Unknown City"}</h2>
      <p>
        Temperature: {data.temp_c ?? 'N/A'}°C / {data.temp_f ?? 'N/A'}°F
      </p>
      <p>Condition: {data.condition ?? 'Unknown'}</p>
    </div>
  );
}


export default WeatherCard;
