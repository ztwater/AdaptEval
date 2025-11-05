from math import pi, asin, sin, degrees
halfpi, twopi = .5 * pi, 2 * pi
sphere_area = lambda R=1.0: 4 * pi * R ** 2

lat_dist = lambda lat, R=1.0: R*(1-sin(lat))

#A = 2*pi*R^2(1-sin(lat))
def sphere_latarea(lat, R=1.0):
    if -halfpi > lat or lat > halfpi:
        raise ValueError("lat must be between -halfpi and halfpi")
    return 2 * pi * R ** 2 * (1-sin(lat))

sphere_lonarea = lambda lon, R=1.0: \
        4 * pi * R ** 2 * lon / twopi

#A = 2*pi*R^2 |sin(lat1)-sin(lat2)| |lon1-lon2|/360
#    = (pi/180)R^2 |sin(lat1)-sin(lat2)| |lon1-lon2|
sphere_rectarea = lambda lat0, lat1, lon0, lon1, R=1.0: \
        (sphere_latarea(lat0, R)-sphere_latarea(lat1, R)) * (lon1-lon0) / twopi


def test_sphere(n_lats=10, n_lons=19, radius=540.0):
    total_area = 0.0
    for i_lons in range(n_lons):
        lon0 = twopi * float(i_lons) / n_lons
        lon1 = twopi * float(i_lons+1) / n_lons
        for i_lats in range(n_lats):
            lat0 = asin(2 * float(i_lats) / n_lats - 1)
            lat1 = asin(2 * float(i_lats+1)/n_lats - 1)
            area = sphere_rectarea(lat0, lat1, lon0, lon1, radius)
            print("{:} {:}: {:9.4f} to  {:9.4f}, {:9.4f} to  {:9.4f} => area {:10.4f}"
                    .format(i_lats, i_lons
                    , degrees(lat0), degrees(lat1)
                    , degrees(lon0), degrees(lon1)
                    , area))
            total_area += area
    print("total_area = {:10.4f} (difference of {:10.4f})"
            .format(total_area, abs(total_area) - sphere_area(radius)))

test_sphere()
