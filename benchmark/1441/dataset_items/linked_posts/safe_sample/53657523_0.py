>>> keywords = ['foo', 'bar', 'bar', 'foo', 'baz', 'foo']

>>> list(dict.fromkeys(keywords))
['foo', 'bar', 'baz']
