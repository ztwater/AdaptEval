def find(key, value):
  for k, v in (value.items() if isinstance(value, dict) else
               enumerate(value) if isinstance(value, list) else []):
    if k == key:
      yield v
    elif isinstance(v, (dict, list)):
      for result in find(key, v):
        yield result
