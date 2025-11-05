In [1]: import glom

In [2]: data = { "id" : "abcde", "key1" : "blah", ... }  # OP example

In [3]: glom.glom(data, '**.id')
Out[3]: ['abcde', 'qwerty', 'xyz', 'fghi', 'asdf', 'yuiop']
