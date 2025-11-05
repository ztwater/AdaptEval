>>> i = []  # instead of an int, i is now a *mutable* object
>>> def f(i=i):
...     print('i =', i)
...
>>> i.append(5)  # instead of *assigning* a new value to i, we're *mutating* it
>>> f()
i = [5]
