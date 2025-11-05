def cubic_interpolate(x0, x, y):
""" Natural cubic spline interpolate function
    This function is licenced under: Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)
    https://creativecommons.org/licenses/by-sa/3.0/
    Author raphael valentin
    Date 25 Mar 2022
"""
xdiff = np.diff(x)
dydx = np.diff(y)
dydx /= xdiff

n = size = len(x)

w = np.empty(n-1, float)
z = np.empty(n, float)

w[0] = 0.
z[0] = 0.
for i in range(1, n-1):
    m = xdiff[i-1] * (2 - w[i-1]) + 2 * xdiff[i]
    w[i] = xdiff[i] / m
    z[i] = (6*(dydx[i] - dydx[i-1]) - xdiff[i-1]*z[i-1]) / m
z[-1] = 0.

for i in range(n-2, -1, -1):
    z[i] = z[i] - w[i]*z[i+1]

# find index (it requires x0 is already sorted)
index = x.searchsorted(x0)
np.clip(index, 1, size-1, index)

xi1, xi0 = x[index], x[index-1]
yi1, yi0 = y[index], y[index-1]
zi1, zi0 = z[index], z[index-1]
hi1 = xi1 - xi0

# calculate cubic
f0 = zi0/(6*hi1)*(xi1-x0)**3 + \
    zi1/(6*hi1)*(x0-xi0)**3 + \
    (yi1/hi1 - zi1*hi1/6)*(x0-xi0) + \
    (yi0/hi1 - zi0*hi1/6)*(xi1-x0)
return f0
