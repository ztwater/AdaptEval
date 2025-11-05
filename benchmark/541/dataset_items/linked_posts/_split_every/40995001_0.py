def one_batch(first_value, iterator, batch_size):
    yield first_value
    for i in xrange(1, batch_size):
        yield iterator.next()

def batch_iterator(iterator, batch_size):
    iterator = iter(iterator)
    while True:
        first_value = iterator.next()  # Peek.
        yield one_batch(first_value, iterator, batch_size)
