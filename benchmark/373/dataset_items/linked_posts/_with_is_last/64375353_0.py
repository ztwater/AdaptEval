_sentinel = object()

def iter_check_last(iterable):
    iterable = iter(iterable)
    current_element = next(iterable, _sentinel)
    while current_element is not _sentinel:
        next_element = next(iterable, _sentinel)
        yield (next_element is _sentinel, current_element)
        current_element = next_element
