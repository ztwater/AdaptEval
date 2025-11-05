>>> l = [0, 1, 2, 3, 4]

>>> n = 2
>>> [l[i: i + min(n, len(l)-i)] for i in range(len(l)-n+1)]
>>> [[0, 1], [1, 2], [2, 3], [3, 4]]
>>>
>>> n = 3
>>> [l[i: i + min(n, len(l)-i)] for i in range(len(l)-n+1)]
>>> [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
>>>
>>> n = 4
>>> [l[i: i + min(n, len(l)-i)] for i in range(len(l)-n+1)]
>>> [[0, 1, 2, 3], [1, 2, 3, 4]]
>>>
>>> n = 5
>>> [l[i: i + min(n, len(l)-i)] for i in range(len(l)-n+1)]
>>> [[0, 1, 2, 3, 4]]
>>>
>>> n = 10 # n > len(l)
>>> [l[i: i + min(n, len(l)-i)] for i in range(len(l)-n+1)]
>>> []
