import functools

def dec(cls):
    @functools.wraps(cls, updated=())
    class D(cls):
        decorated = 1
    return D


@dec
class C:
    """doc"""

print(f'{C.__name__=} {C.__doc__=} {C.__wrapped__=}')
