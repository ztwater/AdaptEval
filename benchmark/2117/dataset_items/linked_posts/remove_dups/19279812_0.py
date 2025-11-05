def unique(iterable):
    seen = set()
    seen_add = seen.add
    for element in itertools.ifilterfalse(seen.__contains__, iterable):
        seen_add(element)
        yield element
