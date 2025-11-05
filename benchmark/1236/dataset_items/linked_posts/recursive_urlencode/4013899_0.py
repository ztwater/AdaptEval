a = {'a': 'b', 'c': {'d': 'e'}}

url = urllib.urlencode([('%s[%s]'%(k,v.keys()[0]), v.values()[0] ) if type(v)==dict else (k,v) for k,v in a.iteritems()])

url = 'a=b&c%5Bd%5D=e'
