val = ["axc", "abc", "abc"]
lot = [reduce(lambda a, b: a if a == b else None, x) for x in zip(*val)] + [None]
out = val[0][:lot.index(None)]
