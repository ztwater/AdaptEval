bearing = atan2(sin(long2 - long1)*cos(lat2), cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(long2 - long1))
bearing = degrees(bearing)
bearing = (bearing + 360) % 360
