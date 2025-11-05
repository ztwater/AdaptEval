In [5]: populationSize, sampleSize = 10**8, 10**5

In [6]: %time lst = random.sample(range(populationSize), sampleSize)
CPU times: user 1.89 s, sys: 299 ms, total: 2.19 s
Wall time: 2.18 s

In [7]: %time lst1 = extractSamples(populationSize, sampleSize, [(0, populationSize-1)])
CPU times: user 449 ms, sys: 8.92 ms, total: 458 ms
Wall time: 442 ms
