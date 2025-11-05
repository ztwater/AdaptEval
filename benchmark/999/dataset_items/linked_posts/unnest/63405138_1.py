explode_b = df.explode('B')['B']
explode_c = df.explode('C')['C']
df = df.drop(['B', 'C'], axis=1)
df = df.join([explode_b, explode_c])
