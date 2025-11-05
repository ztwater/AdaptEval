>>> import pprint
>>> 
>>> data = {
...   112762853378: 
...    {'dst': ['10.121.4.136'], 
...     'src': ['1.2.3.4'], 
...     'alias': ['www.example.com']
...    },
...  112762853385: 
...    {'dst': ['10.121.4.136'], 
...     'src': ['1.2.3.4'], 
...     'alias': ['www.example.com']
...    },
...  112760496444: 
...    {'dst': ['10.121.4.136'], 
...     'src': ['1.2.3.4']
...    },
...  112760496502: 
...    {'dst': ['10.122.195.34'], 
...     'src': ['4.3.2.1']
...    },
... }
>>> 
>>> keep = set({repr(sorted(value.items())):key
...             for key,value in data.iteritems()}.values())
>>> 
>>> for key in data.keys():
...     if key not in keep:
...         del data[key]
... 
>>> 
>>> pprint.pprint(data)
{112760496444L: {'dst': ['10.121.4.136'], 'src': ['1.2.3.4']},
 112760496502L: {'dst': ['10.122.195.34'], 'src': ['4.3.2.1']},
 112762853378L: {'alias': ['www.example.com'],
                 'dst': ['10.121.4.136'],
                 'src': ['1.2.3.4']}}
