module = dict()
with open("/path/to/module") as f:
    exec(f.read(), module)
module['foo']()
