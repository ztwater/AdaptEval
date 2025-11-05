def test_doublewrap():
    from util import doublewrap
    from functools import wraps    

    @doublewrap
    def mult(f, factor=2):
        '''multiply a function's return value'''
        @wraps(f)
        def wrap(*args, **kwargs):
            return factor*f(*args,**kwargs)
        return wrap

    # try normal
    @mult
    def f(x, y):
        return x + y

    # try args
    @mult(3)
    def f2(x, y):
        return x*y

    # try kwargs
    @mult(factor=5)
    def f3(x, y):
        return x - y

    assert f(2,3) == 10
    assert f2(2,5) == 30
    assert f3(8,1) == 5*7
