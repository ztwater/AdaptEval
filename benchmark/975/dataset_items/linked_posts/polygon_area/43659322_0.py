def _area_(coords):
    t=0
    for count in range(len(coords)-1):
        y = coords[count+1][1] + coords[count][1]
        x = coords[count+1][0] - coords[count][0]
        z = y * x
        t += z
    return abs(t/2.0)

a=[(5.09,5.8), (1.68,4.9), (1.48,1.38), (4.76,0.1), (7.0,2.83), (5.09,5.8)]
print _area_(a)
