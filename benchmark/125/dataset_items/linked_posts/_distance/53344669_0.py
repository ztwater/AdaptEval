import mpu
def distance(point1, point2):
    return mpu.haversine_distance(point1, point2)

def closest(data, this_point):
    return min(data, key=lambda x: distance(this_point, x))
