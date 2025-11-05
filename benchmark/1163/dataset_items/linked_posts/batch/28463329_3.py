import json
jsonDict = json.loads(text)
data = DotMap(jsonDict)
print data.location.city
