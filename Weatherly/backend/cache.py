# Simple in-memory cache for storing API responses

cache = {}

def get_from_cache(city):
    return cache.get(city)

def add_to_cache(city, data):
    cache[city] = data