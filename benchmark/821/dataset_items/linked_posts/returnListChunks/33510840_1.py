def chunks(li, n):
    if li == []:
        return
    yield li[:n]
    yield from chunks(li[n:], n)
