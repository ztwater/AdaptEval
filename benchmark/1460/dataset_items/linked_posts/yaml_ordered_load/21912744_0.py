a = dict(zip("unsorted", "unsorted"))
s = yaml.safe_dump(a, sort_keys=False)
b = yaml.safe_load(s)

assert list(a.keys()) == list(b.keys())  # True
