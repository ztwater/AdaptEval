zip(*[seq[i:(len(seq) - n + 1 + i)] for i in range(n)])
