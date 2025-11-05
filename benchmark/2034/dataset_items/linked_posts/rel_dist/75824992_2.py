def calc_orthodromic(row):
    try:
        return geopy.distance.geodesic(row["XY"], row["XY_lag"]).m
    except:
        return np.NaN

df['XY'] = list(zip(df["X"], df["Y"]))
df['XY_lag'] = list(zip(df["X_lag"], df["Y_lag"]))

df['distance'] = df.apply(calc_orthodromic, axis=1)
