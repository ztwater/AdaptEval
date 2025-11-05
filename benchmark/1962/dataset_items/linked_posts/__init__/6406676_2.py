@memoized
def f(a, b=5, *args, keyword=10):
    """Intact docstring!"""
    print('f was called!')
    return {'a':a, 'b':b, 'args':args, 'keyword':10}

x=f(0)  
#OUTPUT: f was called!
print(x)
#OUTPUT: {'a': 0, 'b': 5, 'keyword': 10, 'args': ()}                 

y=f(0)
#NO OUTPUT - MEANS MEMOIZATION IS WORKING
print(y)
#OUTPUT: {'a': 0, 'b': 5, 'keyword': 10, 'args': ()}          

print(f.__name__)
#OUTPUT: 'f'
print(f.__doc__)
#OUTPUT: 'Intact docstring!'
