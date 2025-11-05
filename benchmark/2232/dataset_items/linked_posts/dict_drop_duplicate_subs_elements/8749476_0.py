dct = {112762853378: 
   {'dst': ['10.121.4.136'], 
    'src': ['1.2.3.4'], 
    'alias': ['www.example.com']
   },
 112762853385: 
   {'dst': ['10.121.4.136'], 
    'src': ['1.2.3.4'], 
    'alias': ['www.example.com']
   },
 112760496444: 
   {'dst': ['10.121.4.136'], 
    'src': ['1.2.3.4']
   },
 112760496502: 
   {'dst': ['10.122.195.34'], 
    'src': ['4.3.2.1']
   },
   }

def remove_dups (dct):
    reversed_dct = {}
    for key, val in dct.items():
        new_key = tuple(val["dst"]) + tuple(val["src"]) + (tuple(val["alias"]) if "alias" in val else (None,) ) 
        reversed_dct[new_key] = key
    result_dct = {}
    for key, val in reversed_dct.items():
        result_dct[val] = dct[val]
    return result_dct

result = remove_dups(dct)
