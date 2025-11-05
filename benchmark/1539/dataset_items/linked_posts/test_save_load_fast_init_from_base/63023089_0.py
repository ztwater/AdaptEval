#for windows use dill teh same way

import pickle
copy = lambda obj: pickle.loads(pickle.dumps(obj))
