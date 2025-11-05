def testfunc1(xs):
    from functools import partial
    def mypow(x,y): return x ** y
    return list(map(partial(mypow,y=2),xs))
