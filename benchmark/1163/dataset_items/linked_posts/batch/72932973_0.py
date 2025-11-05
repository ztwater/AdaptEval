class Struct(dict):
    def __init__(self, **entries):
        entries = {k: v for k, v in entries.items() if k != "items"}
        dict.__init__(self, entries)
        self.__dict__.update(entries)

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value
        self[attr] = value

# Added benefit of cloning lists and dicts.
def structify(o):
    if isinstance(o, list):
        return [structify(o[i]) for i in range(len(o))]
    elif isinstance(o, dict):
        return Struct(**{k: structify(v) for k, v in o.items()})
    return o
