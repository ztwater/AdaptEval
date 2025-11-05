from math import sqrt
from collections import defaultdict
from joblib import Parallel, delayed

class CallBack(object):
    completed = defaultdict(int)

    def __init__(self, index, parallel):
        self.index = index
        self.parallel = parallel

    def __call__(self, index):
        CallBack.completed[self.parallel] += 1
        print("done with {}".format(CallBack.completed[self.parallel]))
        if self.parallel._original_iterable:
            self.parallel.dispatch_next()

import joblib.parallel
joblib.parallel.CallBack = CallBack

if __name__ == "__main__":
    print(Parallel(n_jobs=2)(delayed(sqrt)(i**2) for i in range(10)))
