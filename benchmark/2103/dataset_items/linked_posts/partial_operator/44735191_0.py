>>> from iteration_utilities import partial
>>> square = partial(pow, partial._, 2)  # the partial._ attribute represents a placeholder
>>> list(map(square, xs))
[1, 4, 9, 16, 25, 36, 49, 64]
