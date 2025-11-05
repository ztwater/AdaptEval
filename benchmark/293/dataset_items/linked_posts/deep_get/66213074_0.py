def safeget(_dct, *_keys):
    if not isinstance(_dct, dict): raise TypeError("Is not instance of dict")
    def foo(dct, *keys):
        if len(keys) == 0: return dct
        elif not isinstance(_dct, dict): return None
        else: return foo(dct.get(keys[0], None), *keys[1:])
    return foo(_dct, *_keys)

assert safeget(dict()) == dict()
assert safeget(dict(), "test") == None
assert safeget(dict([["a", 1],["b", 2]]),"a", "d") == None
assert safeget(dict([["a", 1],["b", 2]]),"a") == 1
assert safeget({"a":{"b":{"c": 2}},"d":1}, "a", "b")["c"] == 2
