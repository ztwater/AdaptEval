from dataprep.clean import clean_lat_long
df = pd.DataFrame({"coord": ["""0°25'30"S, 91°7'W""", """27°29'04.2"N   89°19'44.6"E"""]})

df2 = clean_lat_long(df, "coord", split=True)
# print(df2)
                        coord  latitude  longitude
0           0°25'30"S, 91°7'W   -0.4250   -91.1167
1  27°29'04.2"N\t89°19'44.6"E   27.4845    89.3291
