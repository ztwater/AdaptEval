a = SomeClass()
try:
    return a.fake_prop
except AttributeError:
    return default_value
