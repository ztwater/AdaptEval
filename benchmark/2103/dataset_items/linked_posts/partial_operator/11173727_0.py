from functools import wraps
def foo(a, b, c, d, e):
    print('foo(a={}, b={}, c={}, d={}, e={})'.format(a, b, c, d, e))

def partial_at(func, index, value):
    @wraps(func)
    def result(*rest, **kwargs):
        args = []
        args.extend(rest[:index])
        args.append(value)
        args.extend(rest[index:])
        return func(*args, **kwargs)
    return result

if __name__ == '__main__':
    bar = partial_at(foo, 2, 'C')
    bar('A', 'B', 'D', 'E') 
    # Prints: foo(a=A, b=B, c=C, d=D, e=E)
