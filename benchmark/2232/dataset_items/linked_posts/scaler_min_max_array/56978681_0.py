import joblib
joblib.dump(my_scaler, 'scaler.gz')
my_scaler = joblib.load('scaler.gz')
