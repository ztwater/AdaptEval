nested = {'a': {'b': {'c': 42}}}

print deep_get(nested, ['a', 'b'])
print deep_get(nested, ['a', 'b', 'z', 'z'], default='missing')
