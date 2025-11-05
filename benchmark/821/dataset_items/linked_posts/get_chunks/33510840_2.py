def dec(gen):
    def new_gen(li, n):
        for e in gen(li, n):
            if e == []:
                return
            yield e
    return new_gen

@dec
def chunks(li, n):
    yield li[:n]
    for e in chunks(li[n:], n):
        yield e
