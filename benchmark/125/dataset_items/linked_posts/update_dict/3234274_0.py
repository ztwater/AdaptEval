>>> dict1 = {('level1','level2','levelA'): 0}
>>> dict1['level1','level2','levelB'] = 1
>>> update = {('level1','level2','levelB'): 10}
>>> dict1.update(update)
>>> print dict1
{('level1', 'level2', 'levelB'): 10, ('level1', 'level2', 'levelA'): 0}
