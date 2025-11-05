def grouper(size, iterable):
    i = iter(iterable)
    while True:
        out = []
        try:
            for _ in range(size):
                out.append(i.next())
        except StopIteration:
            yield out
            break
        
        yield out
