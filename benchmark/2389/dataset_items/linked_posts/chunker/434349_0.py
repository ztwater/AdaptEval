def get_chunk(iterable, chunk_size):
    result = []
    for item in iterable:
        result.append(item)
        if len(result) == chunk_size:
            yield tuple(result)
            result = []
    if len(result) > 0:
        yield tuple(result)

for x in get_chunk([1,2,3,4,5,6,7,8,9,10], 3):
    print x

(1, 2, 3)
(4, 5, 6)
(7, 8, 9)
(10,)
