def shuffle_together(x, y):
    assert len(x) == len(y)

    for i in reversed(xrange(1, len(x))):
        # pick an element in x[:i+1] with which to exchange x[i]
        j = int(random.random() * (i+1))
        x[i], x[j] = x[j], x[i]
        y[i], y[j] = y[j], y[i]
