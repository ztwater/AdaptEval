import itertools
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(newfunc.leftmost_args + fargs + newfunc.rightmost_args), **newkeywords)
    newfunc.func = func
    args = iter(args)
    newfunc.leftmost_args = tuple(itertools.takewhile(lambda v: v != Ellipsis, args))
    newfunc.rightmost_args = tuple(args)
    newfunc.keywords = keywords
    return newfunc

>>> print partial(pow, ..., 2, 3)(5) # (5^2)%3
1
>>> print partial(pow, 2, ..., 3)(5) # (2^5)%3
2
>>> print partial(pow, 2, 3, ...)(5) # (2^3)%5
3
>>> print partial(pow, 2, 3)(5) # (2^3)%5
3
