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

filter = list(set(list(input_raw.keys())))

fixedlist = {}

for i in filter:
    fixedlist[i] = logins[i]
