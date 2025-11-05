aprun = ParallelExecutor(n_jobs=5)

a1 = aprun(total=25)(delayed(func)(i ** 2 + j) for i in range(5) for j in range(5))
a2 = aprun(total=16)(delayed(func)(i ** 2 + j) for i in range(4) for j in range(4))
a2 = aprun(bar='txt')(delayed(func)(i ** 2 + j) for i in range(4) for j in range(4))
a2 = aprun(bar=None)(delayed(func)(i ** 2 + j) for i in range(4) for j in range(4))
