def split(a, n):
    k, m = divmod(len(a), n)
    for i in range(n):
        size = k + 1 if i < m else k
        yield a[:size]
        a = a[size:]
