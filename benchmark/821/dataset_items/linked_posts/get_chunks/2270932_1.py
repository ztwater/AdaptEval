def isplitter(l, n):
    l = iter(l)
    chunk = list(islice(l, n))
    while chunk:
        yield chunk
        chunk = list(islice(l, n))
