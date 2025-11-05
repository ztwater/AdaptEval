input_raw = {112762853378:  {'dst': ['10.121.4.136'],
                             'src': ['1.2.3.4'],
                             'alias': ['www.example.com']    },
             112762853385:  {'dst': ['10.121.4.136'],
                             'src': ['1.2.3.4'],
                             'alias': ['www.example.com']    },
             112760496444:  {'dst': ['10.121.4.299'],
                             'src': ['1.2.3.4']    },
             112760496502:  {'dst': ['10.122.195.34'],
                             'src': ['4.3.2.1']    },
             112758601487:  {'src': ['1.2.3.4'],
                             'alias': ['www.example.com'],
                             'dst': ['10.121.4.136']},
             112757412898:  {'dst': ['10.122.195.34'],
                             'src': ['4.3.2.1']    },
             112757354733:  {'dst': ['124.12.13.14'],
                             'src': ['8.5.6.0']},             
             }

for x in input_raw.iteritems():
    print x
print '\n---------------------------\n'

seen = []

for k,val in input_raw.items():
    if val in seen:
        del input_raw[k]
    else:
        seen.append(val)


for x in input_raw.iteritems():
    print x
