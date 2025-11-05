from joblib import Parallel, delayed
from collections import defaultdict

# patch joblib progress callback
class BatchCompletionCallBack(object):
  completed = defaultdict(int)

  def __init__(self, time, index, parallel):
    self.index = index
    self.parallel = parallel

  def __call__(self, index):
    BatchCompletionCallBack.completed[self.parallel] += 1
    print("done with {}".format(BatchCompletionCallBack.completed[self.parallel]))
    if self.parallel._original_iterator is not None:
      self.parallel.dispatch_next()

import joblib.parallel
joblib.parallel.BatchCompletionCallBack = BatchCompletionCallBack
