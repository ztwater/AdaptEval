points = np.flipud(points)
points
>: 
array([[1, 0],
       [1, 5],
       [4, 5],
       [6, 4],
       [5, 0]])


P1 = Polygon(points)

P1.exterior.is_ccw
>: True
