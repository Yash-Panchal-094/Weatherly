export function isValidCityName(city) {
    return /^[a-zA-Z\s]+$/.test(city);
}
