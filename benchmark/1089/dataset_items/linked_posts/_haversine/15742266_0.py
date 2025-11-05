from math import sqrt, cos, radians

R = 6371  # radius of the earth in km
x = (radians(lon2) - radians(lon1)) * cos(0.5 * (radians(lat2) + radians(lat1)))
y = radians(lat2) - radians(lat1)
d = R * sqrt(x*x + y*y)
