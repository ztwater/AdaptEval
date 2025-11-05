X = np.array([[1., 0.], [2., 1.], [0., 0.]])
y = np.array([0, 1, 2])
from sklearn.utils import shuffle
X, y = shuffle(X, y)
