def dictionaryafy(self, in_dict):
    tree = {}
    for key, value in in_dict.items():
        t = tree
        parts = key.split(".")
        for part in parts[:-1]:
            t = t.setdefault(part, {})
        t[parts[-1]] = value
    return tree
