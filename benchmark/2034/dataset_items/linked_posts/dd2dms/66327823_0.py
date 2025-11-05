from dataprep.clean import clean_lat_long
df = pd.DataFrame({"coord": [(45.5003, -122.4420), (5.8833, -162.0833)]})

df2 = clean_lat_long(df, "coord", output_format="dms")
# print(df2)
                 coord                        coord_clean
0  (45.5003, -122.442)  45° 30′ 1.08″ N, 122° 26′ 31.2″ W
1  (5.8833, -162.0833)  5° 52′ 59.88″ N, 162° 4′ 59.88″ W
