def chunks(li, n):
    if li == []:
        return
    yield li[:n]
    for e in chunks(li[n:], n):
        yield e
