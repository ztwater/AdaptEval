chunk_lists = lambda it, n: (l for l in ([],) for i, g in enumerate((it, ((),))) for e in g for l in (l[:len(l) % n] + [e][:1 - i],) if (len(l) % n == 0) != i)
