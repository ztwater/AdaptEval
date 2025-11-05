from numpy import array

n = 3

a = array([1,2])
a.setflags(write=False)
t = [a]*n + [array([1])] # Append spurious array that is not len(a)
r = array(t,dtype=object)
r.setflags(write=False)

assert id(a) == id(t[1]) == id(r[1])
