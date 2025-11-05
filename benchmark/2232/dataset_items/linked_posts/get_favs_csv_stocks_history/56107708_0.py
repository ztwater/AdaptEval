import pickle
# save the model to disk
filename = 'gpr_model.sav'
pickle.dump(gpr, open(filename, 'wb')) 

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
