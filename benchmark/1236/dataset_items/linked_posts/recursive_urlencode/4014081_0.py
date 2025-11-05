d = {'a': 'b', 'c': {'d': 'e'}}
s = json.dumps(d)  # s: '{"a": "b", "c": {"d": "e"}}'
json.loads(s)  # -> d
