import functools

def f(i):
    return i

for i in range(3):    
    f_with_i = functools.partial(f, i)  # important: use a different variable than "f"
    functions.append(f_with_i)
