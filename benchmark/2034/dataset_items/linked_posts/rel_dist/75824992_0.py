X = [0, 1, 1, 0, 0]
Y = [0, 0, 1, 1, 0]

df = pd.DataFrame({"X": X, "Y": Y})

df["X_lag"] = df["X"].shift(1)
df["Y_lag"] = df["Y"].shift(1)


distances = np.sqrt((df['X']-df["X_lag"])**2+(df['Y']-df["Y_lag"])**2)
print(distances)
