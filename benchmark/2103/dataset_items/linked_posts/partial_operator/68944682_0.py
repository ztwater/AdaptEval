class MyPartial:
    def __init__(self, func, *args):
        self._func = func
        self._args = args
        
    def __call__(self, *args):
        return self._func(*args, *self._args) # swap ordering
    
xs = [1,2,3,4,5,6,7,8]
list(map(MyPartial(pow,2),xs))

>>> [1, 4, 9, 16, 25, 36, 49, 64]
