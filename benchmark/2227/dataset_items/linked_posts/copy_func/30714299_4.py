_sum = sum
def sum(iterable, start=0):
    """sum function that works like the regular sum function, but noisy"""
    print('calling the sum function')
    return _sum(iterable, start)
    
