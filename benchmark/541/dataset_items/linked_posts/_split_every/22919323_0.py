from itertools import islice, takewhile, repeat
split_every = (lambda n, it:
    takewhile(bool, (list(islice(it, n)) for _ in repeat(None))))
