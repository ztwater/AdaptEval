def chop(n, iterable):
    iterator = iter(iterable)
    while chunk := list(take(n, iterator)):
        yield chunk


def take(n, iterable):
    iterator = iter(iterable)
    for i in range(n):
        try:
            yield next(iterator)
        except StopIteration:
            return
