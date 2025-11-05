input_raw = {112762853378: 
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
   }
}

result = {}

for key,value in input_raw.items():
    if value not in result.values():
        result[key] = value

print result
