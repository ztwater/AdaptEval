from timeit import timeit
from random import shuffle
from bisect import insort
from itertools import groupby

def original(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def use_first_any(iterable):
    g = groupby(iterable)
    return not any(g) or not any(g)

def next_as_statement(iterable):
    g = groupby(iterable)
    next(g, None)
    return not next(g, False)

def use_first_next(iterable):
    g = groupby(iterable)
    return not next(g, False) or not next(g, False)

funcs = [original, use_first_any, next_as_statement, use_first_next]

for iterable in (), (1,), (1, 2):
    print(f'{iterable = }')
    times = {func: [] for func in funcs}
    for _ in range(1000):
        shuffle(funcs)
        for func in funcs:
            number = 1000
            t = timeit(lambda: func(iterable), number=number) / number
            insort(times[func], t)
    for func in sorted(funcs, key=times.get):
        print(*('%4d ns ' % round(t * 1e9) for t in times[func][:3]), func.__name__)
    print()
