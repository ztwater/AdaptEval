def TDMAsolver(a,b,c,d):
""" This function is licenced under: Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)
    https://creativecommons.org/licenses/by-sa/3.0/
    Author raphael valentin
    Date 25 Mar 2022
    ref. https://www.cfd-online.com/Wiki/Tridiagonal_matrix_algorithm_-_TDMA_(Thomas_algorithm)
"""
n = len(d)

w = np.empty(n-1,float)
g = np.empty(n, float)

w[0] = c[0]/b[0]
g[0] = d[0]/b[0]

for i in range(1, n-1):
    m = b[i] - a[i-1]*w[i-1]
    w[i] = c[i] / m
    g[i] = (d[i] - a[i-1]*g[i-1]) / m
g[n-1] = (d[n-1] - a[n-2]*g[n-2]) / (b[n-1] - a[n-2]*w[n-2])

for i in range(n-2, -1, -1):
    g[i] = g[i] - w[i]*g[i+1]

return g
