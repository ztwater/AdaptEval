from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.externals import joblib


pipeline = make_pipeline(MinMaxScaler(),YOUR_ML_MODEL() )

model = pipeline.fit(X_train, y_train)
