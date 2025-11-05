''' Split a list into "ragged" chunks

    The size of each chunk is either the floor or ceiling of len(seq) / chunks

    chunks can be > len(seq), in which case there will be empty chunks

    Written by PM 2Ring 2017.03.30
'''

def ragged_chunks(seq, chunks):
    size = len(seq)
    start = 0
    for i in range(1, chunks + 1):
        stop = i * size // chunks
        yield seq[start:stop]
        start = stop

# test

def test_ragged_chunks(maxsize):
    for size in range(0, maxsize):
        seq = list(range(size))
        for chunks in range(1, size + 1):
            minwidth = size // chunks
            #ceiling division
            maxwidth = -(-size // chunks)
            a = list(ragged_chunks(seq, chunks))
            sizes = [len(u) for u in a]
            deltas = all(minwidth <= u <= maxwidth for u in sizes)
            assert all((sum(a, []) == seq, sum(sizes) == size, deltas))
    return True

if test_ragged_chunks(100):
    print('ok')
