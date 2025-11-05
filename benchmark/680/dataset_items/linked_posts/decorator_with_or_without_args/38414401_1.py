    @meta_wrap
    def baddecor(f, caller=lambda x: -1*x):
        @functools.wraps(f)
        def _f(*args, **kwargs):
            return caller(f(args[0]))
        return _f

    @baddecor  # used without arg: no problem
    def f_call1(x):
        return x + 1
    assert f_call1(5) == -6

    @baddecor(lambda x : 2*x) # bad case
    def f_call2(x):
        return x + 1
    f_call2(5)  # raises ValueError

    # explicit keyword: no problem
    @baddecor(caller=lambda x : 100*x)
    def f_call3(x):
        return x + 1
    assert f_call3(5) == 600
