def ragged_chunks(seq, chunks):
    size = len(seq)
    start = 0
    for i in range(size, size * chunks + 1, size):
        stop = i // chunks
        yield seq[start:stop]
        start = stop
