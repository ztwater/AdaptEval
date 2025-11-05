from sklearn.preprocessing import MinMaxScaler
data = np.array([1,2,3]).reshape(-1, 1)
scaler = MinMaxScaler()
scaler.fit(data)
print(scaler.transform(data))
