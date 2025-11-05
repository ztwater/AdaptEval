# could use: import pickle... however let's do something else
from sklearn.externals import joblib 

# this is more efficient than pickle for things like large numpy arrays
# ... which sklearn models often have.   

# then just 'dump' your file
joblib.dump(clf, 'my_dope_model.pkl') 
