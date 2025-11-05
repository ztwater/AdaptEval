import matfunc as mt

def perspective_coefficients(self, oldplane, newplane):
    """
    Calculates and returns the transform coefficients needed for a perspective 
    transform, ie tilting an image in 3D.
    Note: it is not very obvious how to set the oldplane and newplane arguments
    in order to tilt an image the way one wants. Need to make the arguments more
    user-friendly and handle the oldplane/newplane behind the scenes.
    Some hints on how to do that at http://www.cs.utexas.edu/~fussell/courses/cs384g/lectures/lecture20-Z_buffer_pipeline.pdf

    | **option** | **description**
    | --- | --- 
    | oldplane | a list of four old xy coordinate pairs
    | newplane | four points in the new plane corresponding to the old points

    """
    # first find the transform coefficients, thanks to http://stackoverflow.com/questions/14177744/how-does-perspective-transformation-work-in-pil
    pb,pa = oldplane,newplane
    grid = []
    for p1,p2 in zip(pa, pb):
        grid.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        grid.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    # then do some matrix magic
    A = mt.Matrix(grid)
    B = mt.Vec([xory for xy in pb for xory in xy])
    AT = A.tr()
    ATA = AT.mmul(A)
    gridinv = ATA.inverse()
    invAT = gridinv.mmul(AT)
    res = invAT.mmul(B)
    a,b,c,d,e,f,g,h = res.flatten()

    # finito
    return a,b,c,d,e,f,g,h
