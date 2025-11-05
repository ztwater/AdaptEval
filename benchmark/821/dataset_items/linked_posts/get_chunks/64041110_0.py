chunk_iters = lambda it, n: ((e for i, g in enumerate(((f,), cit)) for j, e in zip(range((1, n - 1)[i]), g)) for cit in (iter(it),) for f in cit)
