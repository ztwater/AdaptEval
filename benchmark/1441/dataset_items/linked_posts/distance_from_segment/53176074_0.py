import numpy as np


def dist2d(p1, p2, coords):
    ''' Distance from points to a finite line btwn p1 -> p2 '''
    assert coords.ndim == 2 and coords.shape[1] == 2, 'coords is not 2 dim'
    dp = p2 - p1
    st = dp[0]**2 + dp[1]**2
    u = ((coords[:, 0] - p1[0]) * dp[0] + (coords[:, 1] - p1[1]) * dp[1]) / st

    u[u > 1.] = 1.
    u[u < 0.] = 0.

    dx = (p1[0] + u * dp[0]) - coords[:, 0]
    dy = (p1[1] + u * dp[1]) - coords[:, 1]

    return np.sqrt(dx**2 + dy**2)


# Usage:
p1 = np.array([0., 0.])
p2 = np.array([0., 10.])

# List of coordinates
coords = np.array(
    [[0., 0.],
     [5., 5.],
     [10., 10.],
     [20., 20.]
     ])

d = dist2d(p1, p2, coords)

# Single coordinate
coord = np.array([25., 25.])
d = dist2d(p1, p2, coord[np.newaxis, :])
