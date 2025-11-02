def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit with validation."""
    if not isinstance(c, (int, float)):
        raise ValueError("Temperature must be numeric")
    return round((c * 9/5) + 32, 2)

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

