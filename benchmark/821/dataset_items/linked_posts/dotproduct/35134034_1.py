In [2]: p0, p1, p2 = [3.5, 6.7], [7.9, 8.4], [10.8, 4.8]

In [3]: v0 = np.array(p0) - np.array(p1)

In [4]: v1 = np.array(p2) - np.array(p1)

In [5]: v0
Out[5]: array([-4.4, -1.7])

In [6]: v1
Out[6]: array([ 2.9, -3.6])

In [7]: angle = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))

In [8]: angle
Out[8]: 1.8802197318858924

In [9]: np.degrees(angle)
Out[9]: 107.72865519428085
