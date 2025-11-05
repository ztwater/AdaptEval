    def deg_to_dms(deg, type='lat'):
        decimals, number = math.modf(deg)
        d = int(number)
        m = int(decimals * 60)
        s = (deg - d - m / 60) * 3600.00
        compass = {
            'lat': ('N','S'),
            'lon': ('E','W')
        }
        compass_str = compass[type][0 if d >= 0 else 1]
        return '{}º{}\'{:.2f}"{}'.format(abs(d), abs(m), abs(s), compass_str)
