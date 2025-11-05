from scipy.spatial.distance import cdist 
df1_latlon = df1[['lat','lon']]
df2_latlon = df2[['lat', 'lon']]
distanceCalc = cdist(df1_latlon, df2_latlon, metric=haversine)
