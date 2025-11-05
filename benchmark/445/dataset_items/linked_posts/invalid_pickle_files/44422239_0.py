import gzip, pickle
with gzip.open('test.pklz', 'wb') as ofp:
    pickle.dump([1,2,3], ofp)
