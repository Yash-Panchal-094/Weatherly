import pytest
from utils.temp_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

def test_fahrenheit_to_celsius():
    assert round(fahrenheit_to_celsius(32), 1) == 0
    assert round(fahrenheit_to_celsius(212), 1) == 100
