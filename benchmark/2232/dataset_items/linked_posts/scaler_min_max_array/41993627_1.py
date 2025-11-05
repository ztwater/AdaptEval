import pickle
scalerfile = 'scaler.sav'
scaler = pickle.load(open(scalerfile, 'rb'))
test_scaled_set = scaler.transform(test_set)
