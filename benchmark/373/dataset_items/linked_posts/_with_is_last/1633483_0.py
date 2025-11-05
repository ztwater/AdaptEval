def last_iter(it):
    # Ensure it's an iterator and get the first field
    it = iter(it)
    prev = next(it)
    for item in it:
        # Lag by one item so I know I'm not at the end
        yield 0, prev
        prev = item
    # Last item
    yield 1, prev

def test(data):
    result = list(last_iter(data))
    if not result:
        return
    if len(result) > 1:
        assert set(x[0] for x in result[:-1]) == set([0]), result
    assert result[-1][0] == 1

test([])
test([1])
test([1, 2])
test(range(5))
test(xrange(4))

for is_last, item in last_iter("Hi!"):
    print is_last, item
