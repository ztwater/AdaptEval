>>> a = [lambda x=x: x*x for x in range(10)]
>>> for item in a:
>>>     print(item())
0
1
4
9
16
25
36
49
64
81
