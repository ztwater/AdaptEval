In [8]: data = {
   ...:     "people": [
   ...:         {"first_name": "Alice", "last_name": "Adams"},
   ...:         {"first_name": "Bob", "last_name": "Barker"}
   ...:     ]
   ...: }

In [9]: glom(data, ("people", ["first_name"]))
Out[9]: ['Alice', 'Bob']
