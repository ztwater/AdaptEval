>>> import collections
>>> reverse_d = collections.defaultdict(list)
>>> for key, inner_d in d.iteritems():
...     key_str = ''.join(inner_d[k][0] for k in ['dst', 'src', 'alias'] if k in inner_d)
...     reverse_d[key_str].append(key)
... 
>>> duplicates = [keys for key_str, keys in reverse_d.iteritems() if len(keys) > 1]
>>> duplicates
[[112762853385, 112762853378]]
