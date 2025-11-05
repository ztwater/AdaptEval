def find(key, value):
  for k, v in value.items():
    if k == key:
      yield v
    elif isinstance(v, dict):
      for result in find(key, v):
        yield result
    elif isinstance(v, list):
      for d in v:
        for result in find(key, d):
          yield result
