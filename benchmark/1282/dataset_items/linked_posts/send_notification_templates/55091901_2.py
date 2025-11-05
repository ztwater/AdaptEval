>>> i = 0
>>> def f(i=i):
...     pass
>>> f.__defaults__  # this is where the current value of i is stored
(0,)
>>> # assigning a new value to i has no effect on the function's default arguments
>>> i = 5
>>> f.__defaults__
(0,)
