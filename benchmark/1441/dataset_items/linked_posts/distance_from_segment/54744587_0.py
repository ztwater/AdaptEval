def dist(x1,y1,x2,y2,px,py):
    a = np.array([[x1,y1]]).T
    b = np.array([[x2,y2]]).T
    x = np.array([[px,py]]).T
    tp = (np.dot(x.T, b) - np.dot(a.T, b)) / np.dot(b.T, b)
    tp = tp[0][0]
    tmp = x - (a + tp*b)
    d = np.sqrt(np.dot(tmp.T,tmp)[0][0])
    return d, a+tp*b

x1,y1=2.,2.
x2,y2=5.,5.
px,py=4.,1.

d, inters = dist(x1,y1, x2,y2, px,py)
print (d)
print (inters)
