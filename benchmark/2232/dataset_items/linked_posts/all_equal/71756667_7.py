 it = iter(s)
 a = next(it, None)
 return all(a == b for b in it)
