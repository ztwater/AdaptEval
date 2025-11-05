import math

def chunkIt(seq, num):
    seqLen = len(seq)
    total_chunks = math.ceil(seqLen / num)
    items_per_chunk = num
    out = []
    last = 0

    while last < seqLen:
        out.append(seq[last:(last + items_per_chunk)])
        last += items_per_chunk

    return out
