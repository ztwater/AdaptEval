g = 'hello'

def foo():
    return lambda x : (g,x)

f = foo()

print(f('world')); g = 'goodbye'; print(f('earth'))
