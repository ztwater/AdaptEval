# Import Geopy's distance
from geopy import distance

newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)

print(distance.great_circle(newport_ri, cleveland_oh).miles) # If one wants it in km, change `miles` to `km`

[Out]: 536.997990696
