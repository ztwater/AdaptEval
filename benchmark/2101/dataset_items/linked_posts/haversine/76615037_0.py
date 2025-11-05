import math

def haversine_distance(lat1, lon1, lat2, lon2, unit='K'):
    r = 6371  # radius of the earth in kilometers
    if unit == 'M':
        r = 3960  # radius of the earth in miles
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
    math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = r * c
    return distance
