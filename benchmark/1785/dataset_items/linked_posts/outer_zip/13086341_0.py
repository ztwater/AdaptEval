from itertools import chain, repeat

class OuterZipStopIteration(Exception):
    pass

def outer_zip(*args):
    count = len(args) - 1

    def sentinel(default):
        nonlocal count
        if not count:
            raise OuterZipStopIteration
        count -= 1
        yield default

    iters = [chain(p, sentinel(default), repeat(default)) for p, default in args]
    try:
        while iters:
            yield tuple(map(next, iters))
    except OuterZipStopIteration:
        pass


print(list(outer_zip( ("abcd", '!'), 
                      ("ef", '@'), 
                      (map(int, '345'), '$') )))
