import json
from dictor import dictor

with open('test.json') as data: 
    data = json.load(data)

print dictor(data, 'characters.Lonestar.items')

>> [u'space winnebago', u'leather jacket']
