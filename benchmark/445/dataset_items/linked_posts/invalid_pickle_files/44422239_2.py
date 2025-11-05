with gzip.open('test.pklz', 'rb') as ifp:
    print(pickle.load(ifp))

[1, 2, 3]
