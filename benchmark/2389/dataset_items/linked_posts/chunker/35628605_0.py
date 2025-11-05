def chunker(iterable, n):
    """Yield iterable in chunk sizes.

    >>> chunks = chunker('ABCDEF', n=4)
    >>> chunks.next()
    ['A', 'B', 'C', 'D']
    >>> chunks.next()
    ['E', 'F']
    """
    it = iter(iterable)
    while True:
        chunk = []
        for i in range(n):
            try:
                chunk.append(next(it))
            except StopIteration:
                yield chunk
                raise StopIteration
        yield chunk

if __name__ == '__main__':
    import doctest

    doctest.testmod()
