import matplotlib.pyplot as p; p.rcParams['toolbar'] = 'None';

def plt(o, e, b):
    p.figure(figsize=(10, 10), dpi=72, facecolor='w').add_axes([0.05, 0.05, 0.9, 0.9], aspect='equal')
    p.plot(0, 0, marker='x', mew=1, ms=10, c='g', zorder=2, clip_on=False)
    p.gcf().canvas.set_window_title('%f' % e)
    x = np.ravel(o[0].T[0])
    y = np.ravel(o[0].T[1])
    p.xlim(min(x), max(x)) 
    p.ylim(min(y), max(y))
    a = []
    for i, j in np.ndindex(len(o), 2):
        a.append(o[i].T[j])    
    O = p.plot(*a, marker='x', mew=1, ms=10, lw=.25, c='b', zorder=0, clip_on=False)
    O[0].set(c='r', zorder=1)
    if not b:
        O[2].set_color('b')
        O[2].set_alpha(0.4)
    p.axis('off')     
    p.show()

# Fly wings example (Klingenberg, 2015 | https://en.wikipedia.org/wiki/Procrustes_analysis)
arr1 = np.array([[588.0, 443.0], [178.0, 443.0], [56.0, 436.0], [50.0, 376.0], [129.0, 360.0], [15.0, 342.0], [92.0, 293.0], [79.0, 269.0], [276.0, 295.0], [281.0, 331.0], [785.0, 260.0], [754.0, 174.0], [405.0, 233.0], [386.0, 167.0], [466.0, 59.0]])
arr2 = np.array([[477.0, 557.0], [130.129, 374.307], [52.0, 334.0], [67.662, 306.953], [111.916, 323.0], [55.119, 275.854], [107.935, 277.723], [101.899, 259.73], [175.0, 329.0], [171.0, 345.0], [589.0, 527.0], [591.0, 468.0], [299.0, 363.0], [306.0, 317.0], [406.0, 288.0]])

def opa_out(a):
    r, s, t, d = opa(a[0], a[1])
    a[1] = a[1].dot(r) * s + t
    return a, d, False
plt(*opa_out([arr1, arr2, np.matrix.copy(arr2)]))

def gpa_out(a):
    g = gpa(a, -1) 
    D = [avg(a)]
    for i in range(len(a)):
        D.append(a[i].dot(g[0][i]) * g[1][i] + g[2][i])
    return D, sum(g[3])/len(a), True 
plt(*gpa_out([arr1, arr2]))
