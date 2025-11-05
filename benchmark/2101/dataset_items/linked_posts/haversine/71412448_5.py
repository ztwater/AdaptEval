# Import Geopy's distance
from geopy import distance

wellington = (-41.32, 174.81)
salamanca = (40.96, -5.50)
print(distance.distance(wellington, salamanca).km) # If one wants it in miles, change `km` to `miles`

[Out]: 19959.6792674
