from collections import defaultdict

dups = defaultdict(lambda : defaultdict(list))

for key, entry in data.iteritems():
    dups[tuple(entry.keys())][tuple([v[0] for v in entry.values()])].append(key)

for dup_indexes in dups.values():
    for keys in dup_indexes.values():
        for key in keys[1:]:
            if key in data:
                del data[key]
