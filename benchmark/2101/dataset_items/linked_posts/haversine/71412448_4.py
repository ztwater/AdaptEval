from math import radians, cos, sin, atan2, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great-circle distance (in km) between two points
    using their longitude and latitude (in degrees).
    """
    # Radius of the Earth
    r = 6371.0

    # Convert degrees to radians
    # First point
    lat1 = radians(lat1)
    lon1 = radians(lon1)

    # Second point
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return r * c
