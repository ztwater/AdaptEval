>>> from collections import Counter
>>> c = Counter()
>>> c["goodbye"]+=1
>>> c["and thank you"]=42
>>> c["for the fish"]-=5
>>> c
Counter({'and thank you': 42, 'goodbye': 1, 'for the fish': -5})
