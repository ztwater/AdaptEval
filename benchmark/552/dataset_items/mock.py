from base import BaseCamera  # change from .base to base

import math


class MockCamera(BaseCamera):
    def headingBetween(self, lat1, lon1, lat2, lon2):
        # https://stackoverflow.com/a/17662363
        dLon = lon2 - lon1
        y = math.sin(dLon) * math.cos(lat2)
        x = (math.cos(lat1) * math.sin(lat2)) - (math.sin(lat1) * math.cos(lat2) * math.cos(dLon))

        bearing = math.degrees(math.atan2(y, x))

        # Normalise to compass (negative is to the right)
        if bearing < 0:
            bearing = abs(bearing)
            # bearing += 360
        elif bearing > 0:
            bearing = 360 - bearing

        return bearing

