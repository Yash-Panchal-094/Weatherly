export async function getWeather(city) {
  try {
    const response = await fetch(`/api/weather?city=${city}`);
    return await response.json();
  } catch (err) {
    return { error: "Failed to fetch weather data" };
  }
}