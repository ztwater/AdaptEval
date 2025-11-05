>>> line1 = LineString([(0, 0), (0, 1)]) # vertical
>>> line2 = LineString([(0, 0), (1, 0)]) # horizontal
>>> angle_between(line1, line2)
1.5707963267948966
>>> np.degrees(angle_between(line1, line2))
90.0
