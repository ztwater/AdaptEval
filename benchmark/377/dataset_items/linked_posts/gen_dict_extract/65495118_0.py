document = [ { 'taco' : 42 } , { 'salsa' : [ { 'burrito' : { 'taco' : 69 } } ] } ]

>>> print(nested_lookup('taco', document))
[42, 69]
