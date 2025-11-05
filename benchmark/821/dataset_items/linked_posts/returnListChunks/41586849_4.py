def paged_iter(iterat, n):
    itr = iter(iterat)
    deq = None
    try:
        while(True):
            deq = collections.deque(maxlen=n)
            for q in range(n):
                deq.append(next(itr))
            yield (i for i in deq)
    except StopIteration:
        yield (i for i in deq)
