import functools

def f(a,b):
    return a*b

funcs = []

for i in range(0,10):
    funcs.append(functools.partial(f,i))
