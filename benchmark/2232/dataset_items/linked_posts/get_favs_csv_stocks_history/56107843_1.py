from sklearn import svm
from sklearn import datasets

iris = datasets.load_iris()
X, y = iris.data, iris.target

clf = svm.SVC()
clf.fit(X, y)  

##########################
# SAVE-LOAD using joblib #
##########################
import joblib

# save
joblib.dump(clf, "model.pkl") 

# load
clf2 = joblib.load("model.pkl")

clf2.predict(X[0:1])
