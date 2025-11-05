from ndicts.ndicts import NestedDict

dictionary1 = {'level1': {'level2': {'levelA': 0, 'levelB': 1}}}
update = {'level1': {'level2': {'levelB': 10}}}

nd, nd_update = NestedDict(dictionary1), NestedDict(update)
