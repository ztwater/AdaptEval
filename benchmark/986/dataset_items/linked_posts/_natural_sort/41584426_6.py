>>> import natsort
>>> import timeit
>>> l1 = ['Apple', 'corn', 'apPlE', 'arbour', 'Corn', 'Banana', 'apple', 'banana']
>>> l2 = list(map(str, range(30)))
>>> l3 = ["{} {}".format(x,y) for x in l1 for y in l2]
>>> print(timeit.timeit('sorted(l3+["0"], key=NaturalStringA)', number=10000, globals=globals()))
362.4729259099986
>>> print(timeit.timeit('sorted(l3+["0"], key=NaturalStringB)', number=10000, globals=globals()))
189.7340817489967
>>> print(timeit.timeit('sorted(l3+["0"], key=NaturalOrdering.by(OrderingType.PerCharacterSwapCase))', number=10000, globals=globals()))
69.34636392899847
>>> print(timeit.timeit('natsort.natsorted(l3+["0"], alg=natsort.ns.GROUPLETTERS | natsort.ns.LOWERCASEFIRST)', number=10000, globals=globals()))
98.2531585780016
