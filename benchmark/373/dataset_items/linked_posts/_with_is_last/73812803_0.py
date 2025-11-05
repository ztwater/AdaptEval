from typing import TypeVar, Iterable
E = TypeVar('E')

def metait(i: Iterable[E]) -> Iterable[tuple[E, bool, bool]]:

    first = True
    previous = None
    for elem in i:
        if previous:
            yield previous, first, False
            first = False
        previous = elem

    if previous:
        yield previous, first, True
