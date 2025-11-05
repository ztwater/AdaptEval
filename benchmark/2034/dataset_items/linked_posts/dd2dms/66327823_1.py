df = pd.DataFrame({"latitude": [45.5003, 5.8833], "longitude": [-122.4420, -162.0833]})

df2 = clean_lat_long(df, lat_col="latitude", long_col="longitude", output_format="dms")
# print(df2)
   latitude  longitude                 latitude_longitude
0   45.5003  -122.4420  45° 30′ 1.08″ N, 122° 26′ 31.2″ W
1    5.8833  -162.0833  5° 52′ 59.88″ N, 162° 4′ 59.88″ W
