from np.random import permutation
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data #numpy array
y = iris.target #numpy array

# Data is currently unshuffled; we should shuffle 
# each X[i] with its corresponding y[i]
perm = permutation(len(X))
X = X[perm]
y = y[perm]
