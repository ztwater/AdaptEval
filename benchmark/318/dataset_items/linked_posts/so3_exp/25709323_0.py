from numpy import cross, eye, dot
from scipy.linalg import expm, norm

def M(axis, theta):
    return expm(cross(eye(3), axis/norm(axis)*theta))

v, axis, theta = [3,5,0], [4,4,1], 1.2
M0 = M(axis, theta)

print(dot(M0,v))
# [ 2.74911638  4.77180932  1.91629719]
