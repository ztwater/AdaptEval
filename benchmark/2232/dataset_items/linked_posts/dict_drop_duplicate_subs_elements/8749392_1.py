>>> for key, inner_d in d.iteritems():
...     key_str = ''.join(inner_d[k][0] for k in ['dst', 'src', 'alias'] if k in inner_d)
...     reverse_d[key_str] = key
>>> new_d = dict((val, d[val]) for val in reverse_d.itervalues())
