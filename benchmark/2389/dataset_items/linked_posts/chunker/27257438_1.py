class IteratorExhausted(Exception):
    pass

def translate_StopIteration(iterable, to=IteratorExhausted):
    for i in iterable:
        yield i
    raise to # StopIteration would get ignored because this is generator,
             # but custom exception can leave the generator.

def custom_zip(*iterables, reductor=tuple):
    iterators = tuple(map(translate_StopIteration, iterables))
    while True:
        try:
            yield reductor(next(i) for i in iterators)
        except IteratorExhausted: # when any of iterators get exhausted.
            break
