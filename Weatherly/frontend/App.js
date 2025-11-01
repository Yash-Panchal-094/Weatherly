import React, { useState } from "react";
import WeatherCard from "./WeatherCard";
import { getWeather } from "./api";

function App() {
  const [city, setCity] = useState("London");
  const [data, setData] = useState(null);

  const fetchData = async () => {
    const res = await getWeather(city);
    setData(res);
  };

  return (
    <div className="app">
      <h1>Weatherly 🌤️</h1>
      <input
        type="text"
        placeholder="Enter city"
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />
      <button onClick={fetchData}>Get Weather</button>
      {data && <WeatherCard data={data} />}
    </div>
  );
}

export default App;
