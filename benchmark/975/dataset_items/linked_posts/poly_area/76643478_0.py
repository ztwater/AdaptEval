import numpy as np, numpy.linalg as lin

def area(pts):
    ps = np.array([0.5 * lin.det(np.vstack((pts[i], pts[i+1]))) for i in range(len(pts)-1)])
    s = np.sum(ps)
    p1,p2 = pts[-1],pts[0] # cycle back, last pt with the first 
    s += 0.5 * lin.det(np.vstack((p1,p2)))
    return np.abs(s)

points = np.array([[0,0],[10,0],[10,10],[0,10]])
area(points) # 100
