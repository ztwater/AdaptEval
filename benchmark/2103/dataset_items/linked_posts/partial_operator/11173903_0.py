import itertools
print list(itertools.imap(pow, [1, 2, 3], itertools.repeat(2)))
