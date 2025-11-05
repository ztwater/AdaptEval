import json
json_dict = json.loads(text)
data = DotWiz(json_dict)
print data.location.city
